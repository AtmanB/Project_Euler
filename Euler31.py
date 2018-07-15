# Ok that was hard...

def main():
    ways = [1] + [0] * 200
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    print(str(ways[-1]))



if __name__ == "__main__":
    main()