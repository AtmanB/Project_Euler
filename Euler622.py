from project_euler import get_divisors


def main():
    ans = 0
    bar = 2 ** 60
    print(get_divisors(bar - 1))


if __name__ == '__main__':
    main()
