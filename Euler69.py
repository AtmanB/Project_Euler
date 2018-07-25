from Euler47 import prime_factors
from Timer import timethis


@timethis
def main():
    maxim = 0
    ans = 0
    for n in range(2,1000001):
        t = n / phi_function(n)
        if t > maxim:
            maxim = t
            ans = n
    print(ans)


def phi_function(n):
    result = n
    primes = prime_factors(n)
    for prime in primes:
        t = 1 - 1 / prime
        result *= t
    return result

if __name__ == '__main__':
    main()
