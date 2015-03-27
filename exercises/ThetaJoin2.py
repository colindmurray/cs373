#!/usr/bin/env python3

# -------------
# ThetaJoin2.py
# -------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from unittest import main, TestCase

def theta_join_for (r, s, bp) :
    for u in r :
        for v in s :
            if bp(u, v) :
                yield dict(list(u.items()) + list(v.items()))

def theta_join_generator (r, s, bp) :
    return (dict(list(u.items()) + list(v.items())) for u in r for v in s if bp(u, v))

def bind (f) :
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
                list(f(r, s, lambda u, v : u["A"] == v["A"])),
                [{'A': 2, 'B': 5, 'D': 7},
                 {'A': 3, 'B': 6, 'D': 5},
                 {'A': 3, 'B': 6, 'D': 6}])

    return MyUnitTests

theta_join_for_tests       = bind(theta_join_for)
theta_join_generator_tests = bind(theta_join_generator)

if __name__ == "__main__" :
    main()
