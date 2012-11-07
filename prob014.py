#!/usr/bin/python

mmap = {1:1}
ans, max = 0, 0
for i in range(1, 1000000):
    j, t = i, 1
    while True:
        if j == 1:
            if t > max:
                ans, max = i, t
            mmap[i] = t
            break            
        elif j in mmap:
            mmap[i] = t + mmap[j] - 1
            if mmap[i] > max:
                ans, max = i, mmap[i]
            break
        j = 3 * j + 1 if j & 1 else j / 2
        t += 1
print ans

