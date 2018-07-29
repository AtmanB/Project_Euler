from Euler27 import is_prime
from Timer import timethis


def main():
    ans = 0
    max_con = 21
    primes = get_all_primes_until(10000)
    for i in range(len(primes)):
        for j in range(i + 1):
            q = sum(primes[j:len(primes) - 1 - i + j])
            if is_prime(q) and q < 1000000:
                if len(primes) - i > max_con:
                    max_con = len(primes) - i
                    ans = q
    print(ans, max_con)

@timethis
def get_all_primes_until(n):
    primes = [1, 2]
    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    main()
