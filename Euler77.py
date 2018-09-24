from Timer import timethis
from project_euler import sieve_of_eratosthenes


@timethis
def main():

    coins, checker = sieve_of_eratosthenes(100)
    print(coins)
    n = 10
    while True:
        ways = [1] + [0] * n
        for coin in coins[1:]:
            for i in range(len(ways) - coin):
                ways[i + coin] += ways[i]
        if ways[-1] > 5000:
            return n
        n += 1

if __name__ == '__main__':
    print(main())