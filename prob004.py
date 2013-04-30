#!/usr/bin/env python

ans = 0
for x in range(999, 900, -1):
    for y in range(999, 900, -1):
        if ans > x*y:
            break
        s = str(x*y)
        if s == s[::-1]:
            ans = x*y
    if x * 999 < ans:
        break
print ans
