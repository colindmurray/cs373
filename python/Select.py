#!/usr/bin/env python3

# ---------
# Select.py
# ---------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.r = \
            [{"A" : 1, "B" : 4, "C" : 3},
             {"A" : 2, "B" : 5, "C" : 2},
             {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        self.assertEqual(
            list(select(self.r, lambda d : d["B"] > 4)),
            [{'A': 2, 'B': 5, 'C': 2},
             {'A': 3, 'B': 6, 'C': 1}])

    def test_2 (self) :
        self.assertEqual(
            list(select(self.r, lambda d : d["A"] > d["C"])),
            [{'A': 3, 'B': 6, 'C': 1}])

if __name__ == "__main__" :
    main()
