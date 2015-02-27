#!/usr/bin/env python3

"""
CS373: Quiz #16 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What kind of table is needed to represent a many-to-many association?
    [UML Design: Many-to-many]
    (1 pt)

join or junction table
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (5 pts)

[2, 3, 8, 9]
[2, 3, 4, 9]
[2, 3, 4, 5]
[2, 3, 8, 4]
[2, 3, 4, 9]
[3, 4, 8, 2]
[2, 3, 8, 4]
[2, 4, 5, 3]
[2, 3, 4, 5]
"""

def f (x, y, z = 8, t = 9) :
    return [x, y, z, t]

print(f(2, 3))
print(f(2, 3, 4))
print(f(2, 3, 4, 5))
print(f(2, 3, t = 4))
print(f(2, *(3, 4)))
print(f(t = 2, *(3, 4)))
print(f(*(2, 3), t = 4))
print(f(2, t = 3, *(4, 5)))
print(f(2, *(3, 4), t = 5))
