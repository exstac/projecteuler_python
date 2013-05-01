#!/usr/bin/env python

from helpers.utils import fib

for i, f in enumerate(fib()):
    if len(str(f)) == 1000:
        print i + 1
        break
