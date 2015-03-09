#!/usr/bin/env python3

"""
CS373: Quiz #19 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

10
12

16
18

22
24
"""

from operator import add, mul

def bind2nd (bf, y) :
    return lambda x : bf(x, y)

def compose (f, g) :
    return lambda x : f(g(x))

f = compose(bind2nd(add, 1), bind2nd(mul, 3))
g = compose(bind2nd(mul, 3), bind2nd(add, 1))

print(f(3))
print(g(3))
print()

print(f(5))
print(g(5))
print()

print(f(7))
print(g(7))
