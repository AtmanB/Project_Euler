def main():

    for i in range(1, 9):

        for j in range(10 ** i, int((10 ** (i + 1)) / 6)):
            digits = []
            temp_digits = []
            for digit in str(j):
                digits.append(digit)
            digits.sort()
            for digit in str(j * 2):
                temp_digits.append(digit)
            temp_digits.sort()
            if temp_digits == digits:
                temp_digits = []
                for digit in str(j * 3):
                    temp_digits.append(digit)
                temp_digits.sort()
                if temp_digits == digits:
                    temp_digits = []
                    for digit in str(j * 4):
                        temp_digits.append(digit)
                    temp_digits.sort()
                    if temp_digits == digits:
                        temp_digits = []
                        for digit in str(j * 5):
                            temp_digits.append(digit)
                        temp_digits.sort()
                        if temp_digits == digits:
                            temp_digits = []
                            for digit in str(j * 6):
                                temp_digits.append(digit)
                            temp_digits.sort()
                            if temp_digits == digits:
                                print(j)
                                return 0
            # print(digits)


if __name__ == '__main__':
    main()