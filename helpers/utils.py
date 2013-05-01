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
    return sum(i+n/i if n/i != i else i for i in range(1, int(sqrt(n)+1)) if n % i == 0)-n


def lex_perm(a):
    found = 0
    while found != -1:
        yield a
        found = -1
        for i in range(len(a)-2, -1, -1):
            if a[i] < a[i+1]:
                found = i
                break
        if found > -1:
            found2 = found+1
            for i in range(found+1, len(a)):
                if a[i] > a[found] and a[i] < a[found2]:
                    found2 = i
            a[found], a[found2] = a[found2], a[found]
            a = a[0:found+1] + sorted(a[found+1:])
