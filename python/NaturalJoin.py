#!/usr/bin/env python3

# --------------
# NaturalJoin.py
# --------------

# http://en.wikipedia.org/wiki/Relational_algebra#Natural_join_.28.E2.8B.88.29

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
            list(natural_join(r, s)),
            [{'A': 2, 'B': 5, 'D': 7},
             {'A': 3, 'B': 6, 'D': 5},
             {'A': 3, 'B': 6, 'D': 6}])

if __name__ == "__main__" :
    main()
