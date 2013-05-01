#!/usr/bin/env python

from math import sqrt


def sig(n):
    return sum(i + n/i for i in range(1, int(sqrt(n)) + 1) if n % i == 0) - n

print sum(i for i in range(1, 10000) if sig(sig(i)) == i and i != sig(i))
