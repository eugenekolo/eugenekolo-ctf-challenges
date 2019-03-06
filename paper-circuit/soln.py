class Light1(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            setattr(self, key, val)
    @property
    def a(self):
        return not ((self.A or self.B) and self.G)
    @property
    def b(self):
        return (self.C or self.E) and self.S
    @property
    def c(self):
        return self.Q and self.R
    @property
    def d(self):
        return self.I or (self.L and self.A)
    @property
    def e(self):
        return self.H or self.I
    @property
    def f(self):
        return (self.F and self.B) or not self.O
    @property
    def g(self):
        return not ((self.H or self.B) and self.L) or self.G

class Light2(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            setattr(self, key, val)
    @property
    def a(self):
        return not ((self.Q or self.B) and self.G)
    @property
    def b(self):
        return self.C and self.S
    @property
    def c(self):
        return self.P and not self.R
    @property
    def d(self):
        return self.E or (self.G and (self.L and self.A))
    @property
    def e(self):
        return self.H or not self.I
    @property
    def f(self):
        return (self.F or self.J) or not self.O
    @property
    def g(self):
        return not ((self.J or self.B) and self.E) or self.C

class Light3(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            setattr(self, key, val)
    @property
    def a(self):
        return True
    @property
    def b(self):
        return self.S or self.E
    @property
    def c(self):
        return self.N
    @property
    def d(self):
        return self.I or (self.J and self.K)
    @property
    def e(self):
        return self.H and self.F
    @property
    def f(self):
        return self.F and not self.T
    @property
    def g(self):
        return not self.T

class Light4(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            setattr(self, key, val)
    @property
    def a(self):
        return not self.G or self.M
    @property
    def b(self):
        return (self.A or self.B) and (self.M and self.N)
    @property
    def c(self):
        return self.Q and self.L
    @property
    def d(self):
        return self.L and (not self.H or self.E)
    @property
    def e(self):
        return self.B or self.L
    @property
    def f(self):
        return (self.E and self.B) or (self.Q and self.E)
    @property
    def g(self):
        return not (self.B and self.R or self.D)

print("Starting EKSPICE")
print("$$$$$$$$$$$$$$$$")

inp = {}
switches = 'ABCDEFGHIJKLMNOPQRST'
solns = []

import itertools
for bits in itertools.product(range(2), repeat=20):
    for idx, bit in enumerate(bits):
        inp[switches[idx]] = bit

    L1 = Light1(**inp)
    L2 = Light2(**inp)
    L3 = Light3(**inp)
    L4 = Light4(**inp)

    is_f_correct = L1.a and L1.e and L1.f and L1.g and not L1.b and not L1.c and not L1.d
    is_l_correct = L2.d and L2.e and L2.f and not L2.a and not L2.b and not L2.c and not L2.g
    is_a_correct = L3.a and L3.b and L3.c and L3.e and L3.f and L3.g and not L3.d
    is_g_correct = L4.a and L4.c and L4.d and L4.e and L4.f and not L4.b and not L4.g

    if ((is_f_correct and is_l_correct and is_a_correct and is_g_correct)):
        soln = []
        for switch, on in inp.iteritems():
            if on:
                soln.append(switch)

        solns.append(''.join(sorted(soln)))

print("$$$$$$$$$$$$$$")
print("Found %d" % len(solns))
print(solns)
