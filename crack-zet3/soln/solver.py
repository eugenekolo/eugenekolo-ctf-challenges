#!/usr/bin/env python
"""
Solve crack-zet3 challenge for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>
"""
from z3 import *
import sys

vals = []
sol = Solver()
for i in range(21):
    vals.append(Int(str(i)))
    sol.add(Or(And(vals[i] >= 48, vals[i] <= 57), And(vals[i] >= 65, vals[i] <= 125)))

sol.add(vals[8]-vals[13]+vals[19]+vals[9]==104)
sol.add(vals[16]-vals[8]-vals[9]*vals[1]-vals[19]==-4464)
sol.add(vals[2]-vals[2]+vals[14]*vals[15]==2912)
sol.add(vals[13]*vals[2]+vals[6]==4541)
sol.add(vals[7]+vals[7]*vals[4]*vals[2]==211300)
sol.add(vals[12]*vals[15]+vals[15]+vals[14]==3748)
sol.add(vals[18]*vals[19]-vals[20]*vals[4]-vals[13]==-5332)
sol.add(vals[0]*vals[3]*vals[5]==454608)
sol.add(vals[9]*vals[3]-vals[8]==8064)
sol.add(vals[1]-vals[5]*vals[9]-vals[5]+vals[1]==-3082)
sol.add(vals[4]*vals[11]+vals[9]==3511)
sol.add(vals[19]*vals[14]+vals[3]==3091)
sol.add(vals[4]*vals[0]*vals[16]*vals[18]==17567550)
sol.add(vals[17]+vals[16]*vals[19]+vals[13]*vals[7]==6950)
sol.add(vals[7]*vals[4]+vals[14]-vals[8]==3252)
sol.add(vals[17]+vals[10]*vals[0]*vals[11]==212267)
sol.add(vals[16]-vals[15]+vals[17]+vals[12]==138)
sol.add(vals[8]+vals[5]*vals[14]==2742)
sol.add(vals[1]-vals[1]+vals[5]*vals[2]==3120)
sol.add(vals[20]-vals[8]+vals[1]*vals[12]-vals[12]==4691)
sol.add(vals[6]+vals[5]+vals[9]==170)


print(sol.check())
m = sol.model()

# vals = MCA{A0826B45FE84A765}
sys.stdout.write("vals = ")
for d in reversed(m.decls()):
    sys.stdout.write(chr(int(str(m[d]))))
sys.stdout.write('\n')
sys.stdout.flush()
