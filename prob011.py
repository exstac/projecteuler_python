#!/usr/bin/env python

from operator import mul
n = map(int, open('prob011.txt').read(-1).split())
#diag down right, diag down left, straight right, straight down
print max([max(map(lambda a: max(map(lambda b: reduce(mul, b), a)), [[n[x+20*y::21][:4] for y in range(17)] for x in range(17)])),
           max(map(lambda a: max(map(lambda b: reduce(mul, b), a)), [[n[x+20*y::19][:4] for y in range(17)] for x in range(3, 20)])),
           max(map(lambda a: max(map(lambda b: reduce(mul, b), a)), [[n[x+20*y:x+4+20*y] for y in range(20)] for x in range(17)])),
           max(map(lambda a: max(map(lambda b: reduce(mul, b), a)), [[n[x+20*y::20][:4] for y in range(17)] for x in range(20)]))])
