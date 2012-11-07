from primes import gen_sieve

g = gen_sieve()
primes = [g.next()]

def tau(n):
    x = n
    d, i = 1, 0
    while x != 1:
        a = 0
        while x % primes[i] == 0 and x != 1:
            x, a = x/primes[i], a+1
        if a > 0: d *= a+1
        i += 1
        if i+1 > len(primes): primes.append(g.next())
    return d
