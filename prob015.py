#!/usr/bin/env python

from operator import mul


def fac(n):
    return reduce(mul, range(n, 1, -1))

print fac(40) / fac(20)**2
