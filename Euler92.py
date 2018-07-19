from Timer import timethis
# Very slow, needs revision


@timethis
def main():
    ans = 0
    for i in range(1,10000001):
        if number_chain_loop_point(i) == 89:
            ans += 1
    print(ans)




def number_chain_loop_point(n):
    while True:
        m = 0
        for d in str(n):
            m += int(d) ** 2
        n = m
        if n == 1 or n == 89:
            break
    return n


if __name__ == '__main__':
    main()


