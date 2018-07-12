def main():
    ans = 0
    r = list(range(6, 10001))
    for i in r:
        d1 = proper_divisor_sum(i)
        d2 = proper_divisor_sum(d1)
        if (d2 == i) and (d1 != i):
            ans = ans + d1 + i
            if d1 > i:
                r.remove(d1)

    print(ans)




def proper_divisor_sum(n):
    sum = 1
    bar = n
    current = 2
    while current < bar:
        if n % current == 0:

            sum = sum + current + n / current
            if current == n / current:
                sum -= current
            bar = n / current
        current = current + 1
    return sum

if __name__ == '__main__':
    main()
