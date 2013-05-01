#!/usr/bin/env python

from helpers.utils import lex_perm
from itertools import islice

millionth = islice(lex_perm(range(0, 10)), 999999, 1000000).next()
print ''.join(str(x) for x in millionth)
