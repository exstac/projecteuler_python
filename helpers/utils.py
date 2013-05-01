from primes import gen_sieve
from math import sqrt


def tau(n):
    g = gen_sieve()
    primes = [g.next()]
    x = n
    d, i = 1, 0
    while x != 1:
        a = 0
        while x % primes[i] == 0 and x != 1:
            x, a = x/primes[i], a+1
        if a > 0:
            d *= a + 1
        i += 1
        if i + 1 > len(primes):
            primes.append(g.next())
    return d


def sig(n):
    return sum(i + n/i for i in range(1, int(sqrt(n)) + 1) if n % i == 0) - n
