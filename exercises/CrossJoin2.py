#!/usr/bin/env python3

# -------------
# s.CrossJoin2.py
# -------------

# http://en.wikipedia.org/wiki/s.Cartesian_product

from unittest import main, Tests.Case

def cross_join_for (r, s) :
    for u in r :
        for v in s :
            yield dict(u, **v)

def cross_join_generator (r, s) :
    return (dict(u, **v) for u in r for v in s)

def bind (f) :
    class MyUnitTests (Tests.Case) :
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
                [{'r.A': 1, 'B': 4, 's.C': 2, 'D': 7},
                 {'r.A': 1, 'B': 4, 's.C': 3, 'D': 5},
                 {'r.A': 1, 'B': 4, 's.C': 3, 'D': 6},
                 {'r.A': 1, 'B': 4, 's.C': 4, 'D': 6},
                 {'r.A': 2, 'B': 5, 's.C': 2, 'D': 7},
                 {'r.A': 2, 'B': 5, 's.C': 3, 'D': 5},
                 {'r.A': 2, 'B': 5, 's.C': 3, 'D': 6},
                 {'r.A': 2, 'B': 5, 's.C': 4, 'D': 6},
                 {'r.A': 3, 'B': 6, 's.C': 2, 'D': 7},
                 {'r.A': 3, 'B': 6, 's.C': 3, 'D': 5},
                 {'r.A': 3, 'B': 6, 's.C': 3, 'D': 6},
                 {'r.A': 3, 'B': 6, 's.C': 4, 'D': 6}])

    return MyUnitTests

cross_join_for_tests       = bind(cross_join_for)
cross_join_generator_tests = bind(cross_join_generator)

if __name__ == "__main__" :
    main()
