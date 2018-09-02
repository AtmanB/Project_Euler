from Timer import timethis


# main 155.45171809196472
# can reduce this time by cutting the chains early, but bored ;p


def digit_factorial_link(n):
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s = 0
    for d in str(n):
        s += factorials[int(d)]
    return s


def digit_factorial_chain(n):
    chain = [n, ]
    while True:
        next = digit_factorial_link(chain[-1])
        if next not in chain:
            chain.append(next)
        else:
            break
    return chain


@timethis
def main():
    # print(digit_factorial_chain(69))
    counter = 0
    for i in range(3, 10 ** 6):
        if len(digit_factorial_chain(i)) == 60:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
