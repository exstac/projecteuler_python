#!/usr/bin/python

from primes import gen_sieve

gen = gen_sieve()
c = 1

while c <= 10001:
    prime = gen.next()
    c += 1
print prime
