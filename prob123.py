#!/usr/bin/env python

from collections import deque
import sys

from helpers.primes import gen_sieve

n = 1
for p in gen_sieve():
    if n % 2 == 1 and 2*n*p > 10**10:
        print n
        break
    n += 1
