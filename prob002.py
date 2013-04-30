#!/usr/bin/env python

sum = 0
a, b = 1, 1
while a < 4000000:
    sum += a + b
    a, b = a + 2 * b, 2 * a + 3 * b
print sum
