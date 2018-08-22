#!/usr/bin/env python
"""Solution for Eugene Kolo's cutie-keygen from BKP CTF 2017.

cutie-keygen is a reversing challenge that is GUI app made with Qt.
The app prompts for a password, if the password is correct, we'll get the flag.

Reversing the challenge you can find that the password is basically put through a series of
3 routines, that terminate in a comparison of the final result to a stored good.
1) XOR the password, w/ a constant key
2) Encrypt the output of (1) with speck-ecb-128-128 w/ a constant key.
3) Form a matrix out of the result of (2), and multiply it w/ a constant matrix key.
-> Output of (3) must match a stored good.

So we basically have: h(g(f(password)) == N. All the functions are reversible w/ known keys,
so we simply have to go backwards (w/ some data manipulation), and do:
1a) Discover what the input into (3) was, by satisfying a matrix equality
2a) Decrypt the output of (1a) using the constant key used in (2)
3a) XOR decrypt the output of (2a) using the constant key used in (1)

[*] Step 1 matrix solution: [['0x845e', '0x5818', '0xf8fd', '0xd873'], ['0x36ef', '0x1c63',
    '0x4e55', '0x813a'], ['0x2135', '0x66b7', '0xf0ed', '0xc8fa'], ['0xa2f9', '0x8568', '0x7204',
    '0x68be']]
[*] Step 2 decryption solution: [37021, 28919, 61191, 23277, 53157, 21840, 32923, 3351, 57610,
    1869, 42087, 12182, 60600, 21350, 30841, 25642]
[*] Step 3 unshuffle solution: [66, 75, 80, 123, 75, 89, 85, 55, 69, 67, 33, 80, 72, 51, 82, 125]
Flag: BKP{KYU7EC!PH3R}
"""

from z3 import *
from struct import unpack, pack
from speck import SpeckCipher

def solve_matrix(A, B):
    """Solves AX = B, where A and B are known matrices.

    Args:
        A : A known matrix
        B : A known matrix

    Returns:
        X: The matrix that satisfies AX = B
    """
    s = Solver()

    X = [[Int(0), Int(1), Int(2), Int(3)],
         [Int(4), Int(5), Int(6), Int(7)],
         [Int(8), Int(9), Int(10), Int(11)],
         [Int(12), Int(13), Int(14), Int(15)]]

    # Add the truth statements
    for i in xrange(4):
        for j in xrange(4):
            s.add(B[i][j] == A[i][0]*X[0][j] + A[i][1]*X[1][j] + A[i][2]*X[2][j] + A[i][3]*X[3][j])

    if (s.check() == sat):
        model = s.model()
        ans = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        for i in xrange(4):
            for j in xrange(4):
                ans[i][j] = model[X[i][j]].as_long()
        return ans
    else:
        return None

def decrypt_matrix(K0, K1, X):
    # Step 1: Create the cipher object

    # Discovered it's speck-ecb-128-128 through reversing
    speck_cipher = SpeckCipher(K0, K1)

    # TODO(eugenek): These steps are less complicated than they look, my SpeckCipher class just blows,
    # and expects data to come as QWORDS

    # Step 2: Format the matrix into cipher text
    # Flatten the matrix to the cipher blocks, size 128
    # First get 64-bit QWORDs, 2 cipher blocks are formed out of them
    ct_64 = [0,0,0,0]
    for i in xrange(4):
        ct_64[i] = (X[i][0] << 48) | (X[i][1] << 32) | (X[i][2] << 16) | (X[i][3] << 0)
    ct0 = (ct_64[0] << 64) | (ct_64[1])
    ct1 = (ct_64[2] << 64) | (ct_64[3])

    # Step 3: Decrypt the cipher text
    pt0_0, pt0_1 = speck_cipher.decrypt(ct_64[0], ct_64[1])
    pt1_0, pt1_1 = speck_cipher.decrypt(ct_64[2], ct_64[3])
    pt0 = (pt0_0 << 64) | (pt0_1)
    pt1 = (pt1_0 << 64) | (pt1_1)

    # Step 4: Parse the data into a list of shorts
    ptshorts = []
    pt0_str = "%0X" % pt0
    for i in xrange(0, len(pt0_str), 4):
        short = pt0_str[i] + pt0_str[i+1] + pt0_str[i+2] + pt0_str[i+3]
        ptshorts.append(int(short, 16))

    pt1_str = "%0X" % pt1
    for i in xrange(0, len(pt1_str), 4):
        short = pt1_str[i] + pt1_str[i+1] + pt1_str[i+2] + pt1_str[i+3]
        ptshorts.append(int(short, 16))

    return ptshorts

def unshuffle(XK, D):
    ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # Step 1: Reverse some XOR, using a known key
    for i in xrange(0, 16):
        ans[i] = XK[i] ^ D[i]

    return ans


# Util functions
def hex_matrix(m):
    hex_matrix = []
    for row in m:
        hex_matrix.extend([map(hex, row)])

    return hex_matrix


if __name__ == "__main__":
    # See the top of the file for a high level explanation

    # Found from reversing, this is the expected result from the correct entry
    B = [[342868586, 276196100, 719703660, 771095780],
         [607388058, 526903709, 1078504063, 1277609804],
         [380802638, 328226818, 869243743, 752195599],
         [503103844, 346660259, 739251810, 732552923]]


    # Found from reversing, this is the key used w/ matrix multiplication
    A = [[4992,   9722,   3242,   226],
         [1252,  22234,   6753,  4671],
         [9993,    259 ,  3591,   192],
         [8245,   5425,     32,  3527]]

    # Found from reversing, this is the key used w/ the speck cipher
    K0 = 0x16d856af880f0e3a
    K1 = 0xd8e8367c058ff310

    # Found from reversing, this is the key used w/ shuffling the entry
    XK = [0x90df, 0x70bc, 0xef57, 0x5a96,
          0xcfee, 0x5509, 0x80ce, 0x0d20,
          0xe14f, 0x070e, 0xa446, 0x2fc6,
          0xecf0, 0x5355, 0x782b, 0x6457]

    # Step 1: The final auth check involves checking that AX = B, where A and B are known constants, and X is computed.
    # So we must discover the X that satisfies AX = B.
    X = solve_matrix(A, B)
    print("[*] Step 1 matrix solution: " + str(hex_matrix(X)))

    # Step 2: The X matrix is generated after encrypting some data, D, w/ a known key, K.
    # Satisfy the equation Decrypt(D, K) = X, where Decrypt is the decryption routine of the symmetric crypto that is
    # reversed out of the binary, and K is a constant key found through reversing. And D is our unknown.
    D = decrypt_matrix(K0, K1, X)
    print("[*] Step 2 decryption solution: " + str(D))

    # Step 3: The D matrix is generated after some shuffling of the entry data  we must reverse the shuffling
    # using the known key, XK to solve the equation Unshuffle(XK, D).
    ans = unshuffle(XK, D)
    print("[*] Step 3 unshuffle solution: " + str(ans))

    print("Flag: " + ''.join( map(chr, ans)))



