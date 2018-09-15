from math import sqrt, gcd

from Timer import timethis


@timethis
def main(m):
    quadrilaterals = m ** 4
    lattices = 0
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            for c in range(1, m + 1):
                for d in range(1, m + 1):
                    lat = get_lattice_points(a, b, c, d)
                    # print(lat, a,b,c,d)
                    if is_square(lat):
                        # print(a, b, c, d, 'lattices : {}'.format(lat))
                        lattices += 1
    print('All quadrilaterals = {} Answer = {} ========================================='.format(quadrilaterals, lattices))


def lattice_q(x, y):
    if x == y:
        return ((x - 1) ** 2 - (x - 1)) / 2
    elif x > y:
        if x % y == 0:
            return ((x - 1) * (y - 1) - (y - 1)) / 2
        else:
            if gcd(x,y) != 1:
                return (((x - 1) * (y - 1)) - ((gcd(x,y)) - 1)) / 2
            else:
                return (((x - 1) * (y - 1)) / 2)
    elif x < y:
        if y % x == 0:
            return ((x - 1) * (y - 1) - (x - 1)) / 2
        else:
            if gcd(x, y) != 1:
                return (((x - 1) * (y - 1)) - (gcd(x,y) - 1)) / 2
            else:
                return (((x - 1) * (y - 1)) / 2)

def get_lattice_points(a, b, c, d):
    lattices = 1 + (a - 1) + (b - 1) + (c - 1) + (d - 1) + lattice_q(a, b) + lattice_q(b, c) + lattice_q(c,
                                                                                                         d) + lattice_q(
        d, a)
    return lattices


def is_square(n):
    sq = sqrt(n)
    round_sq = int(sq)
    if sq % round_sq == 0:
        return True
    return False


if __name__ == '__main__':
    main(4)
    main(10)
    main(100)

