#!/usr/bin/env python

from operator import mul

print sum(int(c) for c in str(reduce(mul, range(100, 1, -1))))
