#!/usr/bin/env python

from helpers.primes import gen_sieve
from itertools import takewhile

print sum([p for p in takewhile(lambda x: x < 2000000, gen_sieve())])
