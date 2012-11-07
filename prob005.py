#!/usr/bin/python

from itertools import count
from primes import gen_sieve

D = {}
for x in range(2, 21):
    for p in gen_sieve():
        if not p in D: D[p] = 0
        if p > x: break
        for i in count():
            if x % p**i != 0:
                D[p] = i - 1 if i - 1 > D[p] else D[p]
                break
ans = 1
for key, val in D.iteritems():
    ans *= key**val
print ans
