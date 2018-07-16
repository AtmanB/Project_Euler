import re
# https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

def main():
    p_n = 1
    p_d = 1
    for d in range(12, 100):
        if d % 10 == 0:
            continue
        for n in range(11, d):
            if n % 10 == 0:
                continue

            if is_fraction_curious(n, d):

                p_n *= n
                p_d *= d
    print(p_d / p_n)

def is_fraction_curious(n, d):
    for digit in str(n):
        for digit2 in str(d):
            if digit == digit2:
                new_n = re.sub(digit, '', str(n), 1)
                new_d = re.sub(digit2, '', str(d), 1)
                if int(new_n) / float(new_d) == n / float(d):
                    return True
    return False


if __name__ == '__main__':
    main()

