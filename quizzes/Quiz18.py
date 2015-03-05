#!/usr/bin/env python3

"""
CS373: Quiz #18 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. Fill in the TWO blanks below:
    [The Liskov Substitution Principle]
    (2 pts)

    Functions that use pointers or references to <BLANK> classes must be
    able to use objects of <BLANK> classes without knowing it.

base
derived
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

True
False

True
True
"""

class A :
    v = [1, 2, 3]

x = A()

A.v = [4, 5, 6]
print("v" in A.__dict__)
print("v" in x.__dict__)
print()

x.v = [7, 8, 9]
print("v" in A.__dict__)
print("v" in x.__dict__)
