#!/usr/bin/env python

from helpers.utils import tau

ans = 2
while True:
    divs = tau(ans*(ans+1)/2)
    if divs > 500:
        break
    ans += 1
print ans*(ans+1)/2
