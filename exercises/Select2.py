#!/usr/bin/env python3

# ----------
# Select2.py
# ----------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

from unittest import main, TestCase

def select_yield (r, up) :
    for d in r :
        if up(d) :
            yield d

def select_generator (r, up) :
    return (d for d in r if up(d))

def select_filter (r, up) :
    return filter(up, r)

def bind (f) :
    class MyUnitTests (TestCase) :
        def setUp (self) :
            self.r = \
                [{"A" : 1, "B" : 4, "C" : 3},
                 {"A" : 2, "B" : 5, "C" : 2},
                 {"A" : 3, "B" : 6, "C" : 1}]

        def test_1 (self) :
            self.assertEqual(
                list(f(self.r, lambda d : d["B"] > 4)),
                [{'A': 2, 'B': 5, 'C': 2},
                 {'A': 3, 'B': 6, 'C': 1}])

        def test_2 (self) :
            self.assertEqual(
                list(f(self.r, lambda d : d["A"] > d["C"])),
                [{'A': 3, 'B': 6, 'C': 1}])

    return MyUnitTests

select_yield_tests     = bind(select_yield)
select_generator_tests = bind(select_generator)
select_filter_tests    = bind(select_filter)

if __name__ == "__main__" :
    main()
