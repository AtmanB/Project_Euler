from Euler27 import is_prime


def main():
    primes = 0
    number = 10
    ans = 0
    while primes < 11:
        if is_prime(number):
            if is_truncatable_prime(number):
                print(number)
                primes += 1
                ans += number
        number += 1
    print(ans)


def is_truncatable_prime(n):
    flag_right = False
    flag_left = False
    for i in range(len(str(n)) - 1, 0, -1):
        if is_prime(n % (10 ** i)):
            flag_left = True
        else:
            return False
    for j in range(1, len(str(n))):
        if is_prime(int(n / 10 ** j)):
            flag_right = True
        else:
            return False
    if flag_right and flag_left:
        return True
    return False


if __name__ == '__main__':
    main()
