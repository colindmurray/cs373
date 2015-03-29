#!/usr/bin/env python3

# -------------
# ThetaJoin2.py
# -------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from unittest import main, TestCase

def theta_join_for (r, s, up) :
    for u in r :
        for v in s :
            w = dict(u, **v)
            if up(w) :
                yield w

def theta_join_generator (r, s, up) :
    return (dict(u, **v) for u in r for v in s if up(dict(u, **v)))

def cross_join (r, s) :
    return (dict(u, **v) for u in r for v in s)

def select (r, up) :
    return (v for v in r if up(v))

def theta_join_cross_join_select (r, s, up) :
    return select(cross_join(r, s), up)

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
                list(f(r, s, lambda v : v["A"] == v["C"])),
                [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                 {'A': 3, 'B': 6, 'C': 3, 'D': 6}])

    return MyUnitTests

theta_join_for_tests               = bind(theta_join_for)
theta_join_generator_tests         = bind(theta_join_generator)
theta_join_cross_join_select_tests = bind(theta_join_cross_join_select)

if __name__ == "__main__" :
    main()
