from math import factorial
# ok... that was easy AF

def main():
    ans = 0
    for n in range(1, 101):
        for r in range(1, n):
            if select_r_from_n(r, n) > 1000000:
                ans += 1
    print(ans)


def select_r_from_n(r, n):
    return factorial(n) / (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    main()