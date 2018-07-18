import math


def main():
    for i in range(1, 1000000):
        if len(prime_factors(i)) == 4:
            if len(prime_factors(i+1)) == 4:
                if len(prime_factors(i + 2)) == 4:
                    if len(prime_factors(i + 3)) == 4:
                        print(i)
                        break


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors


if __name__ == '__main__':
    main()
