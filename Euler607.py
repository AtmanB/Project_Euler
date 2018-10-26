# Snell's Awesome law

import math
from math import sin, asin, cos, acos

STRAIGHT_PATH = 100
MARSH_STRAIGHT = 50 * (2 ** 0.5)
A = (STRAIGHT_PATH - MARSH_STRAIGHT) / 2
B = A
SPEED, SPEED1, SPEED2, SPEED3, SPEED4, SPEED5 = 10, 9, 8, 7, 6, 5
# a0 = math.pi / 4
GAMMA = 0.1

def main():
    pass


    # # calculate each refracted angle
    # sina1 = sine_rule(sin(a0), 9, 10)
    # a1 = asin(sina1)
    # sina2 = sine_rule(sin(a1), 8, 9)
    # a2 = asin(sina2)
    # sina3 = sine_rule(sin(a2), 7, 8)
    # a3 = asin(sina3)
    # sina4 = sine_rule(sin(a3), 6, 7)
    # a4 = asin(sina4)
    # sina5 = sine_rule(sin(a4), 5, 6)
    # a5 = asin(sina5)
    #
    # # calculate the distance traveled in each marsh section
    #
    # side1 = 10 / sin((a0 * 2) - a1)
    # side2 = 10 / sin((a0 * 2) - a2)
    # side3 = 10 / sin((a0 * 2) - a3)
    # side4 = 10 / sin((a0 * 2) - a4)
    # side5 = 10 / sin((a0 * 2) - a5)
    #
    # # calculate new B side
    # o1 = cosine_rule(cos(a0 - a1), side1*5, MARSH_STRAIGHT)
    # o2 = cosine_rule(cos(a1 - a2), side2*4, side1*4)
    # o3 = cosine_rule(cos(a2 - a3), side3*3, side2*3)
    # o4 = cosine_rule(cos(a3 - a4), side4*2, side3*2)
    # o5 = cosine_rule(cos(a4 - a5), side5, side4)
    #
    # O = o1+o2+o3+o4+o5
    #
    # new_B = cosine_rule(cos((3/4)*math.pi), O/2, B)
    #
    # ans = (2*new_B + side1*(10/9) + side2*(10/8) + side3*(10/7) + side4*(10/6) + side5*2)/10
    # print(ans)


def sine_rule(sine, n, d):
    return (sine * n) / d


def cosine_rule(cosine, side1, side2):
    return (side1 ** 2 + side2 ** 2 - 2*side1*side2*cosine) ** 0.5


if __name__ == '__main__':
    main()
