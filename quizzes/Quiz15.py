#!/usr/bin/env python3

"""
CS373: Quiz #15 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. Fill in the TWO blanks below.
    [The Open-Closed Principle]
    (2 pts)

    Software entities (classes, modules, functions, etc.) should be open
    for <BLANK>, but closed for <BLANK>.

extension
modification
"""

""" ----------------------------------------------------------------------
 2. What is the difference between a surrogate key and a substitute key?
    [Basic UML & SQL: Keys]
    (2 pts)

substitute keys have some descriptive value (e.g. CA, TX, etc.)
"""

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (2 pts)

True
"""

a =  [2, 3, 4]
a += [5]
b =  [2, 3, 4]
b =  b + [5]
print(a == b)
