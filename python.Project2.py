#!/usr/bin/env python3

# -----------
# Project2.py
# -----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

from unittest import main, TestCase

def project_yield (r, *t) :
    for v in r :
        yield {a : v[a] for a in t if a in v}

def project (r, *t) :
    return ({a : v[a] for a in t if a in v} for v in r)

def bind (f) :
    class MyUnitTests (TestCase) :
        def setUp (self) :
            self.r = \
                [{"A" : 1, "B" : 4, "C" : 3},
                 {"A" : 2, "B" : 5, "C" : 2},
                 {"A" : 3, "B" : 6, "C" : 1}]

        def test_1 (self) :
            self.assertEqual(
                list(f(self.r, "B")),
                [{'B': 4},
                 {'B': 5},
                 {'B': 6}])

        def test_2 (self) :
            self.assertEqual(
                list(f(self.r, "A", "C")),
                [{'A': 1, 'C': 3},
                 {'A': 2, 'C': 2},
                 {'A': 3, 'C': 1}])

    return MyUnitTests

project_yield_tests = bind(project_yield)
project_tests       = bind(project)

if __name__ == "__main__" :
    main()
