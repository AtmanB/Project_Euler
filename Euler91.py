import heapq
import math

from Timer import timethis

@timethis
def main(n):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    triangles = 0


    for x1 in range(0,n+1):
        for y1 in range(0, n+1):
            if(x1 == y1 and x1 == 0):
                continue
            for x2 in range(0, n+1):
                for y2 in range(0, n+1):
                    if (x2 == y2 and y2 == 0):
                        continue
                    if (x1 == x2 and y1 == y2):
                        continue
                    if case1(x1, x2, y1, y2) == 0:
                        triangles += 1
                        continue
                    if case2(x1, x2, y1, y2) == 0:
                        triangles += 1
                        continue
                    if case3(x1, x2, y1, y2) == 0:
                        triangles += 1
                        continue

    print(triangles/2)



def case1(x1, x2, y1, y2):
    r = x1*x2 + y1*y2
    return r


def case2(x1, x2, y1, y2):
    r = x1 * (x2 - x1) + y1 * (y2 - y1)
    return r


def case3(x1, x2, y1, y2):
    r = (x2 - x1) * x2 + (y2 - y1) * y2
    return r


if __name__ == '__main__':
    main(50)