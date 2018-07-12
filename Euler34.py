from math import factorial


def main():

    LIMIT = 2540160  # 9!+9!....+9!
    ans = 0
    for i in range(3, LIMIT):
        fsum = 0
        for digit in str(i):

            fsum += factorial(int(digit))
            if fsum == i:
                ans += i

    print(ans)


main()
