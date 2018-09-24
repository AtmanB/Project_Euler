from Timer import timethis
# main 2827.1987063884735, lol Read the forum to learn
# http://mathworld.wolfram.com/PartitionFunctionP.html

#TODO also make a class and make proper python recursive functions

@timethis
def main():
    global l
    l = [0] * (10 ** 6)
    n = 60
    while True:

        check = partition_function_p(n)
        # print(n, check)
        if check % 10 ** 6 == 0:
            return n
        n += 1


def partition_function_p(n):

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif l[n] > 0:
        return l[n]

    result = 0
    sign = 1
    for k in range(1, n+1):

        p1 = int(n - (0.5*k*((3*k)-1)))
        p2 = int(n - (0.5*k*((3*k)+1)))

        result += sign*(partition_function_p(p1) + partition_function_p(p2))
        sign *= -1
    l[n] = result
    return result


if __name__ == '__main__':
    print(main())
