from Euler493 import choose


def red_ways(tiles):
    s = 0
    for i in range(1, (tiles // 2) + 1):
        s += choose(tiles - i, i)
    return s


def green_ways(tiles):
    s = 0
    for i in range(1, (tiles // 3) + 1):
        s += choose(tiles - (2 * i), i)
    return s


def blue_ways(tiles):
    s = 0
    for i in range(1, (tiles // 4) + 1):
        s += choose(tiles - (i * 3), i)
    return s


def main():
    print(red_ways(50) + green_ways(50) + blue_ways(50))
    print(red_ways(50), green_ways(50), blue_ways(50))


if __name__ == '__main__':
    main()