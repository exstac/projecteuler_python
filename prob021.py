#!/usr/bin/env python

from helpers.utils import sig

print sum(i for i in range(1, 10000) if sig(sig(i)) == i and i != sig(i))
