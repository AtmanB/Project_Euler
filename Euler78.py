from Timer import timethis


@timethis
def main():
    n = 4000
    coins = []
    for i in range(n):
        coins.append(i)
    while True:
        ways = [1] + [0] * n
        coins.append(n)
        for coin in coins:
            for i in range(len(ways) - coin):
                ways[i + coin] += ways[i]
        # print(ways[-1])
        if ways[-1] % (10 ** 6) == 0:
            print('-------->', n)
            break
        print(n)
        n += 1


if __name__ == '__main__':
    main()
