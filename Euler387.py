from project_euler import *
from Timer import timethis


@timethis
def main():
    ans = 0
    b = [True] * 10 ** 8
    primes, _ = sieve_of_eratosthenes(10 ** 8)
    print("tables ready")
    # print(primes)
    for pri in primes[5:]:
        # print(pri)
        p = int(str(pri)[:-1])
        if is_strong_harshad(p):
            if is_right_truncatable_harshad(p):
                ans += pri
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

if __name__ == '__main__':
    main()
