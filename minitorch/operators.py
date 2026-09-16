"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x, y):
    return x * y


def id(x):
    return x


def add(x, y):
    return x + y


def neg(x):
    return -x


def lt(x, y):
    return 1 if x < y else 0


def eq(x, y):
    return 1 if x == y else 0


def max(x, y):
    return x if x > y else y


def is_close(x, y):
    return 1 if abs(x - y) < 1e-2 else 0


def sigmoid(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    exp_x = math.exp(x)
    return exp_x / (1 + exp_x)


def relu(x):
    return x if x > 0 else 0


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def log_back(x, d):
    return d / x


def inv(x):
    return 1 / x


def inv_back(x, d):
    return -d / (x * x)


def relu_back(x, d):
    return d if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn):
    def apply(values):
        return [fn(value) for value in values]
    return apply


def zipWith(fn):
    def apply(left, right):
        return [fn(x, y) for x, y in zip(left, right)]
    return apply


def reduce(fn, start):
    def apply(values):
        result = start
        for value in values:
            result = fn(result, value)
        return result

    return apply


negList = map(neg)
addLists = zipWith(add)
sum = reduce(add, 0)
prod = reduce(mul, 1)
