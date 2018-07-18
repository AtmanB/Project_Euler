import itertools


def main():
    ans = []
    true_ans = []
    true_true_ans = 0
    pandigitals = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[362880:]
    primes = [2, 3, 5, 7, 11, 13, 17]
    for number in pandigitals:
        flag = False
        idx = 1
        for prime in primes:
            if (number[idx] * 100 + number[idx + 1] * 10 + number[idx + 2]) % prime == 0:
                flag = True
            else:
                flag = False
                break
            idx += 1
        if flag:
            ans.append(number)
    for n in ans:
        t = ''
        for d in n:
            t += str(d)
        true_ans.append(t)
    for n in true_ans:
        true_true_ans += int(n)
    print(true_true_ans)


if __name__ == '__main__':
    main()

# print(int('01234567'))
