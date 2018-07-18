from Euler27 import is_prime
from Euler50 import get_all_primes_until


def main():
    primes = get_all_primes_until(10000)[168:]
    for step in range(1111,5000):
        for prime in primes:
            if is_prime(prime + step) and is_prime(prime + 2 * step):
                if is_permutation(prime, prime + step) and is_permutation(prime, prime + 2 * step):
                    print(prime, prime + step, prime + step * 2)

    # print(primes)


def is_permutation(a, b):
    if a != b and len(str(a)) == len(str(b)):
        digits = []
        for digit in str(a):
            digits.append(digit)
        for digit in str(b):
            if digit in digits:
                digits.remove(digit)
            else:
                return False
        return True
    return False

if __name__ == '__main__':
    main()

# if is_permutation(7112345, 4531112):
#     print('ok')