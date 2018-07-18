def main():
    ans = 0
    for number in range(10, 10000):
        if is_lychrel_number(number, 50):
            ans += 1
    print(ans)

def is_lychrel_number(n, LIMIT):
    for i in range(LIMIT):
        n += get_palindrome(n)
        if is_palindrome(n):
            return False
    return True


def get_palindrome(n):
    palin = ''
    for d in reversed(str(n)):
        palin += d
    return int(palin)


def is_palindrome(n):
    if n == get_palindrome(n):
        return True
    else:
        return False


if __name__ == '__main__':
    main()

#
# if is_palindrome(11):
#     print('ok')