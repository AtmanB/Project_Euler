from Timer import timethis
from project_euler import is_reduced_proper_fraction


@timethis
def main():
    ans = 0
    for i in range(1,1000000):
        for j in range(i+1,1000001):
            if is_reduced_proper_fraction(i, j):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()