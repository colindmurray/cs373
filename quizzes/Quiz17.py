#!/usr/bin/env python3

"""
CS373: Quiz #17 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

[2, 3, (), {}]
[(4, 5), {'t': 7, 'z': 6}, (), {}]
[(4, 5), 't', ('z',), {}]
[(4, 5), 3, (), {'t': 7, 'z': 6}]
[4, 5, (), {'t': 7, 'z': 6}]
[7, 4, (5,), {'t': 7, 'z': 6}]
"""

def f (x = 2, y = 3, *z, **t) :
    return [x, y, z, t]

t = (4, 5)
d = {"z" : 6 , "t" : 7}

print(f())
print(f( t,   d))
print(f( t,  *d))
print(f( t, **d))
print(f(*t, **d))
print(f(7, *t, **d))
