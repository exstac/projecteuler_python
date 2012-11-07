#!/usr/bin/python

import math
import primes

big = 600851475143
for x in primes.gen_sieve():
    if big % x == 0:
        big /= x
        if big == 1: break
print x


