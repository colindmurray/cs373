#!/usr/bin/env python3

# ------------
# ThetaJoin.py
# ------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def test (self) :
        r = [{"A" : 1, "B" : 4},
             {"A" : 2, "B" : 5},
             {"A" : 3, "B" : 6}]

        s = [{"A" : 2, "D" : 7},
             {"A" : 3, "D" : 5},
             {"A" : 3, "D" : 6},
             {"A" : 4, "D" : 6}]

        self.assertEqual(
            list(theta_join(r, s, lambda u, v : u["A"] == v["A"])),
            [{'A': 2, 'B': 5, 'D': 7},
             {'A': 3, 'B': 6, 'D': 5},
             {'A': 3, 'B': 6, 'D': 6}])

if __name__ == "__main__" :
    main()
