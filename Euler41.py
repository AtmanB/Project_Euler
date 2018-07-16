import itertools

from Euler27 import is_prime


def main():
    ans = 0
    numbers = list(
        itertools.permutations(['1', '2', '3', '4', '5', '6', '7']))  # there is no pandigital prime with 8/9 digits O_o
    for i in reversed(numbers):
        number = ''
        for digit in i:
            number += digit
        if is_prime(int(number)):
            ans = int(number)
            break
    print(ans)


if __name__ == '__main__':
    main()
