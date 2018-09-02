from Timer import timethis
from project_euler import choose


# main 103.27166175842285 oh mommy oh daddy i am a big old baddie

def number_of_rectangles_fitting_in_grid(m, n):
    s = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s += choose(m - (i - 1), 1) * choose(n - (j - 1), 1)
    return s


@timethis
def main():
    distance = 2000000
    ans = 0
    for i in range(1, 100):
        for j in range(100, i - 1, -1):
            n = number_of_rectangles_fitting_in_grid(i, j)
            if abs(2000000 - n) < distance:
                distance = abs(2000000 - n)

                ans = i * j
                print('distance=', distance, 'answer=', ans, i, 'x', j)
    print(ans)


if __name__ == '__main__':
    main()
