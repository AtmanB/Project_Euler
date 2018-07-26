from Euler55 import get_palindrome
from Timer import timethis


@timethis
def main():
    ans = 0
    i = 11
    while i < 10000000:
        if is_reversible(i):
            ans += 1
            i += 2
        # elif i == 10000:
        #     i += 9 * i
        # elif i == 1000000:
        #     i += 9 * i
        else:
            i += 1
    print(ans)


def is_reversible(n):
    flag = True
    if n % 10 == 0:
        return False
    s = n + get_palindrome(n)

    for d in str(s):
        if int(d) % 2 == 0:
            flag = False
    return flag


if __name__ == '__main__':
    main()