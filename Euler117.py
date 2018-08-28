from Euler493 import set_of_nums


def ways_to_make(n):
    ways = [1] + [0] * n
    for tile in [1, 2, 3, 4]:
        for i in range(len(ways) - tile):
            ways[i + tile] += ways[i]
    print(str(ways[-1]))

def main():
    ways_to_make(5)


if __name__ == '__main__':
    main()