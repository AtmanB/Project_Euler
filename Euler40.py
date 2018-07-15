def main():
    LIMIT = 1000000
    the_number = ''
    current = 1
    ans = 0
    while len(the_number) < LIMIT:
        the_number += str(current)
        current += 1
    ans = int(the_number[0]) * int(the_number[9]) * int(the_number[99]) * int(the_number[999]) * int(the_number[9999]) * int(the_number[99999]) * int(the_number[999999])
    print(ans)


if __name__ == '__main__':
    main()
