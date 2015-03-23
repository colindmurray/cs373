#!/usr/bin/env python3

# ---------
# Select.py
# ---------

from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.r = [
                  {"A" : 1, "B" : 4, "C" : 7},
                  {"A" : 2, "B" : 5, "C" : 8},
                  {"A" : 3, "B" : 6, "C" : 9}]

    def test_1 (self) :
        self.assertEqual(
            list(select(self.r, lambda d : ("A" in d) and (d["A"] > 1))),
            [{'A': 2, 'B': 5, 'C': 8},
             {'A': 3, 'B': 6, 'C': 9}])

    def test_2 (self) :
        self.assertEqual(
            list(select(self.r, lambda d : ("B" in d) and (d["B"] > 5))),
            [{'A': 3, 'B': 6, 'C': 9}])

if __name__ == "__main__" :
    main()
