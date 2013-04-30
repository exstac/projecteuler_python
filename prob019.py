#!/usr/bin/env python

from datetime import date

d = date(1901, 1, 1)
end = date(2000, 12, 31)

ans = 0
while d < end:
    ans = ans + 1 if d.weekday() == 6 else ans
    d = date(d.year + d.month / 12, d.month % 12 + 1, 1)
print ans
