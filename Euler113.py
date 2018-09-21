#https://mathschallenge.net/full/never_decreasing_digits

from math import log10

from Timer import timethis
from project_euler import choose


@timethis
def main(limit):
    digits = log10(limit)

    r = increasing_numbers(digits, 9) + decreasing_numbers(digits, 9) - 9 * digits
    return r


def increasing_numbers(digits, max_digit):
    return choose(digits + max_digit, max_digit) - 1


def decreasing_numbers(digits, max_digit):
    return choose(digits + max_digit + 1, max_digit + 1) - 1 - digits


if __name__ == '__main__':
    ans = main(10 ** 100)
    print(ans)


'''
def inc(max_len):
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ans = sum(dp)
    for l in range(2, max_len):
        new = [sum(dp[:i + 1]) for i in range(10)]
        dp = new
        ans += sum(new)
    return ans

def dec(max_len):
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ans = sum(dp)
    for l in range(2, max_len):
        new = [sum(dp[i:]) for i in range(10)]
        dp = new
        ans += sum(new)
    return ans

def solve(exp):
    return inc(exp + 1) + dec(exp + 1) - 9 * exp

def main():
    print(solve(100))

main()
'''
