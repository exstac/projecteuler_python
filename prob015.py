#!/usr/bin/python

def fac(n):
    ret = 1
    while n > 0:
        ret *= n
        n -= 1
    return ret

print fac(40)/fac(20)**2
