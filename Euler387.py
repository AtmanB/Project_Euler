from Euler27 import is_prime
from Timer import timethis


@timethis
def main():
    # if is_harshad(201):
    #     print('ok')
    # print(str(123456789)[:-1])
    # if is_right_truncatable_harshad(201):
    #     print('ok')
    # if is_strong_harshad(201):
    #      print('ok')
    # if is_prime(5.6):
    #     print('ok', 5.6 % 5)
    # if is_strong_right_truncatable_harshad_prime(2011):
    #         print('ok')

    ans = 0
    # primes = get_all_primes_until((10 ** 6) + 1)
    # for prime in primes:
    #     if is_strong_right_truncatable_harshad_prime(prime):
    #         ans += prime
    # print(ans)

    s_r_h = get_all_strong_right_truncatable_harshads_until(10 ** 13 + 1)

    for h in s_r_h:
        for a in [1, 3, 5, 7, 9]:
            temp = int(str(h) + str(a))
            if is_prime(temp):
                ans += temp
    print(ans)


def is_harshad(n):
    s_d = 0
    for d in str(n):
        s_d += int(d)
    if n % s_d == 0:
        return True
    else:
        return False


def is_right_truncatable_harshad(n):
    flag = True
    for i in range(1, len(str(n))):
        if is_harshad(int(str(n)[:-i])):
            continue
        else:
            flag = False

    return flag


def is_strong_harshad(n):
    s_d = 0
    for d in str(n):
        s_d += int(d)
        p = n / s_d
    if is_prime(p):
        return True
    else:
        return False


def is_strong_right_truncatable_harshad_prime(p):
    if len(str(p)) > 1:
        new_p = int(str(p)[:-1])
    else:
        new_p = p
    if is_harshad(new_p):
        if is_strong_harshad(new_p) and is_right_truncatable_harshad(new_p):
            return True
        else:
            return False
    else:
        return False


@timethis
def get_all_strong_right_truncatable_harshads_until(n):
    harshads = [18]
    i = 20
    while i < n:
        if int(str(i)[0]) % 2 == 0:

            if is_harshad(i):
                if is_strong_harshad(i) and is_right_truncatable_harshad(i):
                    harshads.append(i)
            i += 1
        else:
            i += 10 ** (len(str(i)) - 1)
    return harshads
'''

abcde, a+b+c+d+e 2ds 1-18 3ds 1-27 

'''

if __name__ == '__main__':
    main()
