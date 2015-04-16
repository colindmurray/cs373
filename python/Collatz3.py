#!/usr/bin/env python3

from sys import stdin, stdout

def collatz_read (r) :
    return ([int(v) for v in s.split()] for s in r)

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def max_cycle_length (i, j) :
    if i > j :
        i, j = j, i
    v = 0
    for n in range(i, j + 1) :
        c = cycle_length(n)
        if c > v :
            v = c
    return v

def collatz_eval (a) :
    return ([i, j, max_cycle_length(i, j)] for i, j in a)

def collatz_print (a) :
    return (str(i) + " " + str(j) + " " + str(v) + "\n" for i, j, v in a)

def collatz_solve (r, w) :
    for s in collatz_print(collatz_eval(collatz_read(r))) :
        w.write(s)

if __name__ == "__main__" :
    collatz_solve(stdin, stdout)
