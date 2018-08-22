#!/usr/bin/python
# Flag is not in a file.

import datetime
import random
import string
import hashlib
from sys import modules
from threading import Thread
from imp import acquire_lock

DEBUG = True

def validation(attempt):
    if DEBUG:
        return True

    isValid = False
    # REMOVEME They can do `()+,.1=A-Za-z[]_~: might need to add ;
    nochrs = [33,34,35,36,37,38,42,45,47,48,50,51,52,53,54,55,56,57,59,60,62,63,64,92,94,96,123,124,125]
    for i in attempt:
        if ord(i) in nochrs:
            isValid = False
            break
        else:
            isValid = True

    return isValid

def is_not_a_robot(attempt, captcha):
    if DEBUG:
        return True
    
    maybe = hashlib.sha256(attempt).hexdigest()
    if maybe[0:5] == captcha.lower():
        return True

    return False


captcha = ''
for c in range(5):
    captcha += random.SystemRandom().choice(string.hexdigits)

print("I'll execute what you give me, but you must prove you're not a robot: %s" % captcha.lower())
attempt = raw_input("$ ")
if validation(attempt):
    if is_not_a_robot(attempt, captcha):
        if not DEBUG:     
            # Remove import
            x = Thread(target=acquire_lock, args=())
            x.start()
            x.join()
        
            # Remove imported stuff
            del x, acquire_lock, Thread, random, string, hashlib
        
            # Remove modules
            #for k, v in modules.iteritems():
            #    if v == None:
            #        continue
            #    v.__dict__.clear()
            #del k,v
            modules.clear()
            del modules

            # Delete everything else!
            del __builtins__, __doc__, __file__, __name__, __package__

        # Have fun!
        exec 'print ' + attempt

