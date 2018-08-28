import itertools
from math import factorial


def set_of_nums(goal, n, min, max):
    range_ = range(min, max + 1)
    r = []
    for i in itertools.product(range_, repeat=n):
        if sum(i) == goal:
            r.append(i)
    return r


def choose(n, k):
    if n < k:
        return 0
    return factorial(n) / (factorial(k) * factorial(n - k))


def ways_to_get_colors(c):
    if c <= 0:
        return 0
    d = (choose((c - 1) * 10, 20) * choose(c, c - 1))
    ways = (choose(c * 10, 20) - d) * choose(7, c)
    return ways


def chance_of_colors(n):
    return ways_to_get_colors(n) / choose(70, 20)


def chance_of_colors2(c, pulls, balls, b_p_c):
    """

    :param c: number of colors i want
    :param pulls: number of balls to pull
    :param balls: total balls
    :param b_p_c: balls_per_color
    :return:
    """

    random_pulls = set_of_nums(pulls, c, b_p_c)
    d = len(random_pulls)
    total_chance = 0
    diminishing_balls = balls
    for i in random_pulls:
        chance = 1
        for j in i:
            for k in range(1, j + 1):
                chance *= (11 - k) / diminishing_balls
                diminishing_balls -= 1
        diminishing_balls = balls
        total_chance += chance
    return total_chance


def ways_to_get_colors2(n):
    set_ = set_of_nums(20, n, 10)
    temp_ways = len(set_) * (factorial(7) / (factorial(n) * factorial(7 - n)))
    multiplier = 0
    for s in set_:
        multiplier_t = 1
        for i in s:
            multiplier_t *= factorial(10) / (factorial(i) * factorial(10 - i))
        multiplier += multiplier_t
    return temp_ways * multiplier


def main():

    print(ways_to_get_colors(2))
    # print(ways_to_get_colors(3))
    # print(ways_to_get_colors(7))
    # print(chance_of_colors(2))
    # print(chance_of_colors(3))
    # print(chance_of_colors(4))
    # print(chance_of_colors(7))
    ans = 0
    ans2 = 0
    for i in range(2, 8):
        ans += i * chance_of_colors(i)
        ans2 += chance_of_colors(i)
    print(ans)
    print(ans2)

    print(7 * (1 - choose(60, 20) / choose(70, 20)))
    # print(set_of_nums(20, 7, 10))
    # print(chance_of_colors(2, 20, 70, 10) * (factorial(7)/(factorial(5) * factorial(2))))
    # print(chance_of_colors(3, 20, 70, 10) * (factorial(7)/(factorial(3) * factorial(4))))
    # print(chance_of_colors(4, 20, 70, 10) * (factorial(7)/(factorial(4) * factorial(3))))
    # print(chance_of_colors(5, 20, 70, 10) * (factorial(7)/(factorial(5) * factorial(2))))
    # print(chance_of_colors(6, 20, 70, 10) * 7)
    # print(chance_of_colors(7, 20, 70, 10))
    # ways = factorial(70) / (factorial(20) * factorial(50))
    # p2 = ways_to_get_colors(2) / ways
    # p3 = ways_to_get_colors(3) / ways
    # p4 = ways_to_get_colors(4) / ways
    # p5 = ways_to_get_colors(5) / ways
    # p6 = ways_to_get_colors(6) / ways
    # p7 = ways_to_get_colors(7) / ways
    #
    # print(p2, p3, p4, p5, p6, p7)
    # print(p2 + p3 + p4 + p5 + p6 + p7)


if __name__ == '__main__':
    main()
