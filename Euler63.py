# Very easy
from Timer import timethis


@timethis
def main():
    ans = 0
    for base in range(1, 10):
        power = 1
        while len(str(base ** power)) >= power:
            if power == len(str(base ** power)):
                ans += 1
            power += 1
    print(ans)


if __name__ == '__main__':
    main()
