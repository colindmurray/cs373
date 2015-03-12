#!/usr/bin/env python3

"""
CS373: Quiz #20 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. Fill in the blank below.
    [The Dependency Inversion Principle]
    (2 pts)

    High level modules should not depend upon low level modules. Both
    should depend on <BLANK>.

abstractions
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

function
function
function
decorator_2
"""

def decorator_1 (f) :
    def g (n) :
        return f(n)
    return g

def f1 (n) :
    return (3 * n) + 1

print(type(f1))
assert(f1(3) == 10)

f1 = decorator_1(f1)

print(type(f1))
assert(f1(3) == 10)

class decorator_2 :
    def __init__ (self, f) :
        self.f = f

    def __call__ (self, n) :
        return self.f(n)

def f2 (n) :
    return (3 * n) + 1

print(type(f2))
assert(f2(3) == 10)

f2 = decorator_2(f2)

print(type(f2))
assert(f2(3) == 10)
