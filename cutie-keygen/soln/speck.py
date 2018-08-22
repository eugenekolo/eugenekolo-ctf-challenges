#!/usr/bin/env python
"""Speck cipher implementation
Only works on a single 128-bit block at the moment, with a 128-bit key.
Refer to https://eprint.iacr.org/2013/404.pdf for algorithm details.

Author: Eugene Kolo
Website: eugenekolo.com
"""

def mask(x, mask=0xffffffffffffffff):
    return x & mask

def rcs(x, n, size):
    x = mask(((x << (size - n)) | (x >> n)), 2**size-1)
    return x

def lcs(x, n, size):
    x = mask(((x >> (size - n)) | (x << n)), 2**size-1)
    return x

class SpeckCipher:
    def __init__(self, key0, key1):
        """
        """
        self.key0 = key0
        self.key1 = key1
        self.block_size = 128
        self.key_size = 128
        self.key_sched = self.key_schedule()

    def encrypt(self, pt0, pt1):
        """Encrypt round using SPECK, based on published pseudocode:
            #define LCS _lrotl //left circular shift
            #define RCS _lrotr //right circular shift
            #define u64 unsigned long long
            #define R(x,y,k) (x=RCS(x,8), x+=y, x^=k, y=LCS(y,3), y^=x)
            void Speck128ExpandKeyAndEncrypt(u64 pt[], u64 ct[], u64 K[])
            {
            u64 i,B=K[1],A=K[0];
            ct[0]=pt[0]; ct[1]=pt[1];
            for(i=0; i<32; i++){R(ct[1], ct[0], A); R(B, A, i);}
            }
        """
        ct0 = pt1
        ct1 = pt0
        for i in xrange(0, 32):
            round_key = self.key_sched[i]
            ct1, ct0 = self.encrypt_round(ct1, ct0, round_key)

        return ct1, ct0

    def decrypt(self, ct0, ct1):
        """Decrypt round using Speck.
        """
        B = self.key0
        A = self.key1
        pt0 = ct1
        pt1 = ct0
        for i in reversed(range(0, 32)):
            round_key = self.key_sched[i]
            pt1, pt0 = self.decrypt_round(pt1, pt0, round_key)

        return pt1, pt0

    def key_schedule(self):
        B = self.key0
        A = self.key1
        key_sched = [A]
        for i in xrange(0, 32):
            B, A = self.encrypt_round(B, A, i) # Key schedule
            key_sched.append(A)
        return key_sched

    def encrypt_round(self, x, y, k):
        x = rcs(x, 8, 64)
        x = mask(x+y)
        x = mask(x^k)
        y = lcs(y, 3, 64)
        y = mask(y^x)
        return x, y

    def decrypt_round(self, x, y, k):
        """The symmetric reverse of encrypt_round.
        """
        y = mask(y^x)
        y = rcs(y, 3, 64)
        x = mask(x^k)
        x = mask(x-y + 2**64) % 2**64
        x = lcs(x, 8, 64)
        return x, y

if __name__ == "__main__":
    # Test speck128-128, test vectors from IACR publication: https://eprint.iacr.org/2013/404.pdf
    k0 = 0x0f0e0d0c0b0a0908
    k1 = 0x0706050403020100
    pt_good0 = 0x6c61766975716520
    pt_good1 = 0x7469206564616d20
    ct_good0 = 0xa65d985179783265
    ct_good1 = 0x7860fedf5c570d18

    cipher = SpeckCipher(k0, k1)
    ct0, ct1 = cipher.encrypt(pt_good0, pt_good1)
    assert(ct0 == ct_good0)
    assert(ct1 == ct_good1)
    print("Speck encrypt passed!")

    pt0, pt1 = cipher.decrypt(ct0, ct1)
    assert(pt0 == pt_good0)
    assert(pt1 == pt_good1)
    print("Speck decrypt passed!")
