#!/usr/bin/env python3

# --------------
# Decorators2.py
# --------------

def cache_1 (f) :
    d = {}
    def g (n) :
        if n in d :
            return d[n]
        v = f(n)
        d[n] = v
        return v
    return g

@cache_1
def cycle_length_1 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class cache_2 :
    def __init__ (self, f) :
        self.f = f
        self.d = {}

    def __call__ (self, n) :
        if n in self.d :
            return self.d[n]
        v = self.f(n)
        self.d[n] = v
        return v

@cache_2
def cycle_length_2 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def test (f) :
    assert f( 1) == 1
    assert f( 5) == 6
    assert f(10) == 7

print("Decorators2.py")

test(cycle_length_1)
test(cycle_length_2)

print("Done.")
