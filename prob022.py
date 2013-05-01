#!/usr/bin/env python

with open('prob022.txt') as f:
    ans = 0
    for i, name in enumerate(sorted(f.readline().split(','))):
        ans += (i + 1) * sum(map(lambda x: ord(x) - 64, name[1:-1]))
    print ans
