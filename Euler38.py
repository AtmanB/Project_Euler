def main():
    ans = 0
    all_pans = []
    for i in range(1,10000):
        n = 1
        number = ''
        while len(number) < 9:
            number += str(n * i)
            n += 1
        if len(number) == 9:
            if is_pandigital(int(number)):
                all_pans.append(number)
                if int(number) > ans:
                    ans = int(number)

    print(ans)
    print(all_pans)


def is_pandigital(n):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digit in str(n):
        if digit in numbers:
            numbers.remove(digit)
        else:
            return False
        if not numbers:
            return True


if __name__ == '__main__':
    main()

# if is_pandigital(124356987):
#     print('ok')
