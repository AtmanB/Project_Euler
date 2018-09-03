from Timer import timethis


@timethis
def main():
    min_ = 2 / 5
    max_ = 3 / 7
    ans = 0
    d = 1000000
    for n in range(500000, 2, -1):
        while n / d < max_:
            d -= 1
        if min_ < n / (d + 1) < max_:
            min_ = n / (d + 1)
            ans = n
    print(ans)


if __name__ == '__main__':
    main()
