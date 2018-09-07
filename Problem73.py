from math import gcd

from Timer import timethis


def is_reduced_proper_fraction(n, d):
    if gcd(n, d) == 1:
        return True
    else:
        return False

@timethis
def main():
    llimit = 1/3
    ulimit = 1/2
    ans = 0
    for n in range(6000, 1, -1):
        d = 12000
        while d > 0:
            if llimit < n / d < ulimit:
                if is_reduced_proper_fraction(n, d):
                    ans += 1
            d -= 1
    print(ans)



if __name__ == '__main__':
    main()