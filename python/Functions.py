#!/usr/bin/env python3

# ------------
# Functions.py
# ------------

from functools import reduce
from types     import FunctionType, LambdaType, MethodType

print("Functions.py")

def plus_1 (x, y) :
    return x + y

assert type(plus_1) is FunctionType
assert hasattr(plus_1, "__call__")
assert plus_1(2, 3) == 5
assert reduce(plus_1, [2, 3, 4]) == 9

plus_2 = lambda x, y : x + y

assert type(plus_2) is LambdaType
assert hasattr(plus_2, "__call__")
assert plus_2(2, 3) == 5
assert reduce(plus_2, [2, 3, 4]) == 9

class Plus_3 (object) :
    def my_call (self, x, y) :
        return x + y

assert type(Plus_3()) is Plus_3
assert Plus_3().my_call(2, 3) == 5

assert type(Plus_3.my_call) is FunctionType
assert hasattr(Plus_3.my_call, "__call__")
#Plus_3.my_call(2, 3) # TypeError: unbound method my_call() must be called with Plus_3 instance as first argument (got int instance instead
assert Plus_3.my_call(Plus_3(), 2, 3) == 5
#reduce(Plus_3.my_call, [2, 3, 4]) # TypeError: unbound method my_call() must be called with Plus_3 instance as first argument (got int instance instead

assert type(Plus_3().my_call) is MethodType
assert str(Plus_3().my_call)[1:6] == "bound"
assert hasattr(Plus_3().my_call, "__call__")
assert Plus_3().my_call(2, 3) == 5
assert reduce(Plus_3().my_call, [2, 3, 4]) == 9

class Plus_4 (object) :
    @staticmethod
    def my_call (x, y) :
        return x + y

assert type(Plus_4.my_call) is FunctionType
assert hasattr(Plus_4.my_call, "__call__")
assert Plus_4.my_call(2, 3) == 5
assert reduce(Plus_4.my_call, [2, 3, 4]) == 9

class Plus_5 (object) :
    def __call__ (self, x, y) :
        return x + y

assert type(Plus_5()) is Plus_5
assert hasattr(Plus_5(), "__call__")
assert Plus_5()(2, 3) == 5
assert reduce(Plus_5(), [2, 3, 4]) == 9

print("Done.")
