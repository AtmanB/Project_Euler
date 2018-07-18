from math import sqrt

from Euler45 import get_pentagonal_number


def main():
    pentagonals = []
    for i in range(1, 10000):
        pentagonals.append(get_pentagonal_number(i))

    _break_ = False
    for d in range (1, 1148):
        for i in range(9999 - d):
            if is_pentagonal(pentagonals[i] + pentagonals[i + d]) and is_pentagonal(pentagonals[i + d] - pentagonals[i]):
                print(d, pentagonals[i + d] - pentagonals[i]) #ONLY I understood that it wanted the distance and not the actual number?
                _break_ = True
                break
        if _break_:
            break


def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()


if __name__ == '__main__':
    main()

# if is_pentagonal(12):
#     print('ok')