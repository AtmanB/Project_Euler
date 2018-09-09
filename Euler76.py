from Timer import timethis

# the recursive methods didnt work so i refactored the coin problem as it is basically the same, problem 31


@timethis
def main():
    ways = [1] + [0] * 100
    coins = []
    for i in range(1, 100):
        coins.append(i)
    for coin in coins:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    print(str(ways[-1]))


def partitions(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        s = 0
        i = int(n)
        for k in range(1, i + 1):
            s += ((-1) ** (k + 1)) * (partitions(n - 0.5 * k * (3 * k - 1)) + partitions(n - 0.5 * k * (3 * k + 1)))
        return s


if __name__ == '__main__':
    main()
