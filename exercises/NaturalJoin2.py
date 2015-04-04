#!/usr/bin/env python3

# ---------------
# NaturalJoin2.py
# ---------------

# http://en.wikipedia.org/wiki/Relational_algebra#Natural_join_.28.E2.8B.88.29

from ThetaJoin2 import theta_join
from unittest   import main, TestCase

def match (u, v) :
    for a in u :
        for b in v :
            if (a == b) and (u[a] == v[b]) :
                return True
    return False

def natural_join_yield (r, s) :
    for u in r :
        for v in s :
            if match(u, v) :
                yield dict(u, **v)

def natural_join (r, s) :
    return (dict(u, **v) for u in r for v in s if match(u, v))

def natural_join_theta_join (r, s) :
    return theta_join(r, s, match)

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
                list(f(r, s)),
                [{'A': 2, 'B': 5, 'D': 7},
                 {'A': 3, 'B': 6, 'D': 5},
                 {'A': 3, 'B': 6, 'D': 6}])

    return MyUnitTests

natural_join_yield_tests      = bind(natural_join_yield)
natural_join_tests            = bind(natural_join)
natural_join_theta_join_tests = bind(natural_join_theta_join)

if __name__ == "__main__" :
    main()
