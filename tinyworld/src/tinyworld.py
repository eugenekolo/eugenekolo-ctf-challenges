#!/usr/bin/env python

import subprocess
import os
from time import sleep
from random import randint

print("Flag is flag.txt")
print("Let's have some interactive fun.")
print("I'll execute any small world you give me.")
key = raw_input("Give me an env key: ")
value = raw_input("Give me an env value: ")
cmd = ""
while (len(cmd) != 5 or not cmd.isalnum()):
    cmd = raw_input("Give me a 5 char cmd (no special chars!): ")
env = {}
env[key] = value

random_num = randint(0,100000)

process = subprocess.Popen(['/usr/bin/tmux', 'new-session', '-c', '/opt/challenge', '-d', '-s', str(random_num)], env=env)
process.wait()
process = subprocess.Popen(['/usr/bin/tmux', 'send-keys', '-t', str(random_num), cmd, 'KPEnter'])
process.wait()
sleep(3)
subprocess.Popen(['/usr/bin/tmux', 'kill-session', '-t', str(random_num)])