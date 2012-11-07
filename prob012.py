#!/usr/bin/python

from primes import gen_sieve
from math import sqrt
from eulerutils import tau

gen = gen_sieve()
prims = [gen.next()]


ans = 2
while True:
    divs = tau(ans*(ans+1)/2)
    if divs > 500: break
    ans += 1    
print ans*(ans+1)/2
