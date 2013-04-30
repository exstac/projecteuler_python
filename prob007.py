#!/usr/bin/env python

from helpers.primes import gen_sieve

gen = gen_sieve()
c = 1

while c <= 10001:
    prime = gen.next()
    c += 1
print prime
