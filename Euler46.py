from Euler27 import is_prime
from Euler50 import get_all_primes_until

# https://stackoverflow.com/questions/12572362/get-a-string-after-a-specific-substring


def main():
    for i in range (9, 100000000000000 , 2):
        if not goldbach(i) and not is_prime(i):
            print(i)
            break


def goldbach(n):
    primes = get_all_primes_until(n)
    flag = False
    for prime in primes:
        q = (n - prime) / 2
        if str(q ** 0.5).split('.', 1)[1] == '0':     # bitches im smart
            flag = True

    return flag


if __name__ == '__main__':
    main()
