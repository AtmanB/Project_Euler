def main():
    t = 1
    p = 1
    h = 1
    tri = get_triangle_number(t)
    pen = get_pentagonal_number(p)
    hex = get_hexagonal_number(h)
    flag = True
    while flag:

        while hex >= pen:

            while pen >= tri:
                if hex == pen and pen == tri:
                    print(t, tri)
                    if t > 285:
                        flag = False
                t += 1
                tri = get_triangle_number(t)
            p += 1
            pen = get_pentagonal_number(p)

        h += 1
        hex = get_hexagonal_number(h)


def get_triangle_number(n):
    return (n * (n + 1)) / 2


def get_pentagonal_number(n):
    return (n * (3 * n - 1)) / 2


def get_hexagonal_number(n):
    return n * (2 * n - 1)


if __name__ == '__main__':
    main()
