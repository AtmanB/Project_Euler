from Timer import timethis


@timethis
def main():
    digits = 2
    n = 5
    cubes_digits = []
    cubes = []
    permuts_wanted = 5
    flag = True
    while flag:
        digits += 1
        while len(str(n ** 3)) == digits:
            cubes.append(n ** 3)
            n += 1
        for c in cubes:
            digits_list = []

            for d in str(c):
                digits_list.append(int(d))
            digits_list.sort()
            cubes_digits.append(digits_list)
        idx = 0
        for l in cubes_digits:
            if cubes_digits.count(l) == permuts_wanted:
                print(cubes[idx])
                flag = False
                break
            idx += 1
        cubes.clear()
        cubes_digits.clear()


if __name__ == '__main__':
    main()




