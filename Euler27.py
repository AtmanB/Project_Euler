def main():
    A = range(-999, 1000)
    B = range(-1000, 1001)
    T = [0, 0]
    print(T)
    for a in A:
        for b in B:
            n = 0
            while True:
                x = quadratic_formula(n, a, b)

                if is_prime(x):

                    if n > T[0]:
                        T[0] = n
                        T[1] = a * b
                    n += 1
                else:
                    break
    print(T[1])


def quadratic_formula(n, a, b):
    x = (n ** 2) + (a * n) + b
    return x


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == '__main__':
    main()
