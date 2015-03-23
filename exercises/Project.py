#!/usr/bin/env python3

# ----------
# Project.py
# ----------

from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.r = [
                  {"A" : 1, "B" : 4, "C" : 7},
                  {"A" : 2, "B" : 5, "C" : 8},
                  {"A" : 3, "B" : 6, "C" : 9}]

    def test_1 (self) :
        self.assertEqual(
            list(project(self.r, "B")),
            [{'B': 4},
             {'B': 5},
             {'B': 6}])

    def test_1 (self) :
        self.assertEqual(
            list(project(self.r, "A", "C")),
            [{'A': 1, 'C': 7},
             {'A': 2, 'C': 8},
             {'A': 3, 'C': 9}])

if __name__ == "__main__" :
    main()
