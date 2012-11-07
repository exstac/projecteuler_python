#!/usr/bin/python

for a in range(1, 500):
    a2 = a**2
    for b in range(a+1, 500):
        if 1000>a+b: break;
        if a2+b**2==(1000-b-a)**2:
            print a*b*(1000-b-a)
            exit()
