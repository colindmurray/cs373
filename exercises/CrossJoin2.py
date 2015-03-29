#!/usr/bin/env python3

# -------------
# CrossJoin2.py
# -------------

# http://en.wikipedia.org/wiki/Cartesian_product

from unittest import main, TestCase

def cross_join_for (r, s) :
    for u in r :
        for v in s :
            yield dict(u, **v)

def cross_join_generator (r, s) :
    return (dict(u, **v) for u in r for v in s)

def bind (f) :
    class MyUnitTests (TestCase) :
        def test (self) :
            r = [{"A" : 1, "B" : 4},
                 {"A" : 2, "B" : 5},
                 {"A" : 3, "B" : 6}]

            s = [{"C" : 2, "D" : 7},
                 {"C" : 3, "D" : 5},
                 {"C" : 3, "D" : 6},
                 {"C" : 4, "D" : 6}]

            self.assertEqual(
                list(f(r, s)),
                [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
                 {'A': 1, 'B': 4, 'C': 3, 'D': 5},
                 {'A': 1, 'B': 4, 'C': 3, 'D': 6},
                 {'A': 1, 'B': 4, 'C': 4, 'D': 6},
                 {'A': 2, 'B': 5, 'C': 2, 'D': 7},
                 {'A': 2, 'B': 5, 'C': 3, 'D': 5},
                 {'A': 2, 'B': 5, 'C': 3, 'D': 6},
                 {'A': 2, 'B': 5, 'C': 4, 'D': 6},
                 {'A': 3, 'B': 6, 'C': 2, 'D': 7},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 6},
                 {'A': 3, 'B': 6, 'C': 4, 'D': 6}])

    return MyUnitTests

cross_join_for_tests       = bind(cross_join_for)
cross_join_generator_tests = bind(cross_join_generator)

if __name__ == "__main__" :
    main()
