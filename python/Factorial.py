#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.4/library/math.html

from math     import factorial
from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def test_0 (self) :
        self.assertEqual(factorial(0), 1)

    def test_1 (self) :
        self.assertEqual(factorial(1), 1)

    def test_2 (self) :
        self.assertEqual(factorial(2), 2)

    def test_3 (self) :
        self.assertEqual(factorial(3), 6)

    def test_4 (self) :
        self.assertEqual(factorial(4), 24)

    def test_5 (self) :
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__" :
    main()
