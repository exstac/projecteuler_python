#!/usr/bin/python

from primes import gen_sieve

sum = 0
for p in gen_sieve():
    if p > 2000000: break;
    sum+=p
print sum
