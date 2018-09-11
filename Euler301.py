from Timer import timethis


@timethis
def main(bar):
    ans = 0
    for i in range(1, bar + 1):
        if not i ^ (i * 2) == (i * 3):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main(2 ** 30)