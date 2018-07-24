# https://stats.stackexchange.com/questions/3614/how-to-easily-determine-the-results-distribution-for-multiple-dice
# Fs,n(k)=∑i=k−n+1i=1Fs,1(i)Fs,n−1(k−i)


def main():
    d4_results = get_possible_results(4, 9)
    d6_results = get_possible_results(6, 6)
    d4_result_probs = []
    for i in d4_results:
        d4_result_probs.append(probability_to_get_result(4, 9, i))
    d6_result_probs = []
    for i in d6_results:
        d6_result_probs.append(probability_to_get_result(6, 6, i))

    chance_to_win_d6_result_with_d4s = []

    for result in d6_results:
        if result < d4_results[0]:
            chance_to_win_d6_result_with_d4s.append(sum(d4_result_probs))
        elif result == d4_results[len(d4_results) - 1]:
            chance_to_win_d6_result_with_d4s.append(0)
        else:
            chance_to_win_d6_result_with_d4s.append(sum(d4_result_probs[d4_results.index(result) + 1:]))
    ans = []
    for i in range(len(d6_result_probs)):
        ans.append(d6_result_probs[i] * chance_to_win_d6_result_with_d4s[i])
    print(sum(ans))


def probability_to_get_result(s, n, k):
    '''

    :param s: sides on dice
    :param n: number of rolls
    :param k: total result
    :return: ways of getting the result
    '''

    SUM = 0
    if s * n >= k and k >= 1:
        if n == 1:
            return 1 / s

        for i in range(1, k - n + 2):
            temp = probability_to_get_result(s, 1, i) * probability_to_get_result(s, n - 1, k - i)
            SUM += temp
        return SUM
    else:
        return 0


def get_possible_results(s, n):
    '''

    :param s: sides on dice
    :param n: number of dice
    :return: list of results
    '''

    results = []
    for i in range(n, n * s + 1):
        results.append(i)
    return results


if __name__ == '__main__':
    main()
