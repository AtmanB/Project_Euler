def main():
    ans = 0
    max_ways = 0
    for i in range(3, 1001):
        ways = ways_to_make_right_triangle(i)
        if ways > max_ways:
            max_ways = ways
            ans = i
    print(ans)


def ways_to_make_right_triangle(perimeter):
    ways = 0
    for b in range(1, int(perimeter / 2)):
        for c in range(1, (perimeter / 2)):
            if (((b ** 2) + (c ** 2)) ** 0.5) + b + c == perimeter:
                ways += 1

    # for a in range(1, perimeter):
    #     for b in range(1, perimeter - a):
    #         for c in range(1, perimeter - a - b):
    #             if (a ** 2 == (b ** 2) + (c ** 2)) and (a + b + c == perimeter):
    #                 ways += 1
    return ways


if __name__ == '__main__':
    main()