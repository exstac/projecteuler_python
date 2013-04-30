#!/usr/bin/env python

with open('prob018.txt') as nums:
    lines = [map(int, line.split()) for line in reversed(nums.readlines())]

last_line = []
for line in lines:
    if len(last_line) > 0:
        line = [a + b for a, b in zip(line, last_line)]
    last_line = []
    for i in range(len(line) - 1):
        last_line.append(line[i] if line[i] > line[i + 1] else line[i + 1])

print line[0]
