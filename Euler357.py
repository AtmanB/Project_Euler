from Timer import timethis
from project_euler import sieve_of_eratosthenes
# 259.04800152778625


@timethis
def main():
    sum1 = 0
    primes, prime_table = sieve_of_eratosthenes(10 ** 8)
    print("tables ready")
    for p in primes[1:]:
        n = p - 1
        i = 1
        flag = True
        while i <= n ** 0.5:
            if n % i == 0:
                if not prime_table[int(i + n / i)]:
                    flag = False
                    break
            i += 1
        if flag:
            sum1 += n
    print(sum1)


if __name__ == '__main__':
    main()
