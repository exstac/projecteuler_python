#!/usr/bin/env python

from operator import mul

n = map(int, list(open('prob008.txt').readline()[:-1]))
print max([reduce(mul, n[i:i+5]) for i in range(len(n)-5)])
