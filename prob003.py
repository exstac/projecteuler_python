#!/usr/bin/env python

import helpers.primes as primes

big = 600851475143
for x in primes.gen_sieve():
    big = big / x if big % x == 0 else big
    if big == 1:
        break
print x
