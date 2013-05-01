#!/usr/bin/env python

from helpers.utils import sig

ab = [i for i in range(1, 28123) if sig(i) > i]
ab_s = set(ab)


def is_sum(n):
    for i in ab:
        if i > n:
            return False
        if (n - i) in ab_s:
            return True
    return False

print sum(i for i in range(1, 28123) if not is_sum(i))
