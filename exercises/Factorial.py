#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.4/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from sys       import version
from timeit    import timeit
from unittest  import main, TestCase

# recursive procedure
# linear recursive process
def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_range_for (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_range_reduce (n) :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

class MyUnitTests (TestCase) :
    def test_0 (self) :
        self.assertEqual(f(0), 1)

    def test_1 (self) :
        self.assertEqual(f(1), 1)

    def test_2 (self) :
        self.assertEqual(f(2), 2)

    def test_3 (self) :
        self.assertEqual(f(3), 6)

    def test_4 (self) :
        self.assertEqual(f(4), 24)

    def test_5 (self) :
        self.assertEqual(f(5), 120)

if __name__ == "__main__" :
    main()
