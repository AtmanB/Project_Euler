from Timer import timethis


def f_634(n):
    total = 0
    b = 2
    a1 = int((n / b ** 3) ** 0.5)
    the_numbers = []
    while n / b ** 3 >= 4:
        a = int((n / b ** 3) ** 0.5)
        total += (int((n / b ** 3) ** 0.5) - 1)
        for i in range(2, a + 1):
            the_numbers.append((i ** 2) * (b ** 3))
            # if len(the_numbers) > 10000000:
            #     total += len(set(the_numbers))
            #     the_numbers.clear()

        b += 1
    # total += len(set(the_numbers))
    if (total - len(set(the_numbers))) != 0:
        p = n / (total - len(set(the_numbers)))
    else:
        p = 1
    return total, a1, b - 1, total - len(set(the_numbers)), p

@timethis
def main():
    print(f_634(3 * (10 ** 6)))
    print(f_634(100))
    print(f_634(2 * 10 ** 4))
    print(f_634(4 * 10 ** 8))
    # print(f_634(9 * 10 ** 18))


if __name__ == '__main__':
    main()
