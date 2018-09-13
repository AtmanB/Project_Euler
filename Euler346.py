from math import sqrt


def main(n):
    m = int(sqrt(n))
    print(m)
    ans = []
    for i in range(2, m + 1):
        current = 1 + i + i ** 2
        power = 3
        while current < n:
            ans.append(current)
            current += i ** power
            power += 1

    print(sum(set(ans)) + 1)


if __name__ == '__main__':
    main(10 ** 12)