# OK THAT WAS SMART
# https://docs.python.org/3.7/library/decimal.html

from decimal import *

getcontext().prec = 10000


def main():
    max = 0
    ans = 0
    for i in range(1, 1000):
        l = get_decimal_recurring_cycle_length(1, i)
        if l > max:
            max = l
            ans = i
    print(max, ans)


def get_decimal_recurring_cycle_length(n, d):
    numenator = Decimal(n)
    denominator = Decimal(d)
    s = str(numenator / denominator)[2:]
    for i in range(1, len(s)):
        # print(s[-i - 1: -1], s[(-2 * i) - 1: -i - 1])
        if s[-i - 1: -1] == s[(-2 * i) - 1: -i - 1]:  # start from the end of it and ignore last because... it rounds up
            return i
    return 0


if __name__ == '__main__':
    main()
