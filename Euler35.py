from Euler27 import is_prime


def main():
    counter = 0
    for number in range(2, 1000000):

        if is_circular_prime(number):
            counter += 1

    print(counter)


def is_circular_prime(n):
    if is_prime(n):
        flag = True
        for i in range(1, len(str(n))):

            if not is_prime(int(str(n)[-i:] + str(n)[:-i])):
                flag = False
        return flag
    else:
        return False


if __name__ == '__main__':
    main()
