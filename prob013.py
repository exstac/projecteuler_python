#!/usr/bin/env python

print str(sum([int(l[:11]) for l in open('prob013.txt')]))[:10]
