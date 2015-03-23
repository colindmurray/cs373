#!/usr/bin/env python3

"""
CS373: Quiz #22 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

ab\naab
a
\n
aa
"""

from re import search

s = "b ab\naab 123"
m = search("(a+)b([^a]*)(a+)b", s)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
