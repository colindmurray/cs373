#!/usr/bin/env python3

# -------------
# ThetaJoin2.py
# -------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from unittest import main, TestCase

def theta_join_yield (r, s, bp) :
    for u in r :
        for v in s :
            if bp(u, v) :
                yield dict(u, **v)

def theta_join (r, s, bp) :
    return (dict(u, **v) for u in r for v in s if bp(u, v))

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
                list(f(r, s, lambda u, v : u["A"] == v["C"])),
                [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 6}])

    return MyUnitTests

theta_join_yield_tests = bind(theta_join_yield)
theta_join_tests       = bind(theta_join)

if __name__ == "__main__" :
    main()
