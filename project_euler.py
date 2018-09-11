import itertools
import math
import re
from decimal import *
from math import sqrt


def max_sum_path(triangle):
    row_idx = len(triangle) - 2
    for row in reversed(triangle[:(len(triangle) - 1)]):
        for i in range(len(row)):
            row[i] = row[i] + max([triangle[row_idx + 1][i], triangle[row_idx + 1][i + 1]])
            triangle[row_idx][i] = row[i]
        row_idx = row_idx - 1
    return triangle[0][0]


def proper_divisor_sum(n):
    sum = 1
    bar = n
    current = 2
    while current < bar:
        if n % current == 0:

            sum = sum + current + n / current
            if current == n / current:
                sum -= current
            bar = n / current
        current = current + 1
    return sum

def get_divisors(n):
    bar = n
    current = 2

    rel = [1,]
    rer = [n]
    while current < bar:
        if n % current == 0:
            rel.append(current)
            rer = [n // current] + rer
            # sum = sum + current + n / current
            if current == n / current:
                rel.pop()
            bar = n / current
        current = current + 1
    return rel + rer

def get_divisors_up_to_sqrt(n):
    bar = n ** 0.5
    current = 2

    rel = [1,]
    # rer = [n]
    while current < bar:
        if n % current == 0:
            rel.append(current)
            # rer = [n // current] + rer
            # # sum = sum + current + n / current
            # if current == n / current:
            #     rel.pop()
            # bar = n / current
        current = current + 1
    return rel


def get_abundant_numbers(n):
    list_of = []
    for i in range(6, n + 1):
        if proper_divisor_sum(i) > i:
            list_of.append(i)
    return list_of

def abundant_number_combos(abuns):
    list_of = []
    for i in abuns:
        for j in abuns:
            if i + j < 28124:
                list_of.append(i + j)
    list2 = list(set(list_of))
    return list2

def get_decimal_recurring_cycle_length(n, d):
    numenator = Decimal(n)
    denominator = Decimal(d)
    s = str(numenator / denominator)[2:]
    for i in range(1, len(s)):
        # print(s[-i - 1: -1], s[(-2 * i) - 1: -i - 1])
        if s[-i - 1: -1] == s[(-2 * i) - 1: -i - 1]:  # start from the end of it and ignore last because... it rounds up
            return i
    return 0
def quadratic_formula(n, a, b):
    x = (n ** 2) + (a * n) + b
    return x


def is_prime(n):
    if n % int(n) == 0:
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True
    else:
        return False
def distinct_powers(a, b):
    powers = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            powers.append(i ** j)

    return list(set(powers))
def is_fraction_curious(n, d):
    for digit in str(n):
        for digit2 in str(d):
            if digit == digit2:
                new_n = re.sub(digit, '', str(n), 1)
                new_d = re.sub(digit2, '', str(d), 1)
                if int(new_n) / float(new_d) == n / float(d):
                    return True
    return False
def is_circular_prime(n):
    if is_prime(n):
        flag = True
        for i in range(1, len(str(n))):

            if not is_prime(int(str(n)[-i:] + str(n)[:-i])):
                flag = False
        return flag
    else:
        return False
def is_truncatable_prime(n):
    flag_right = False
    flag_left = False
    for i in range(len(str(n)) - 1, 0, -1):
        if is_prime(n % (10 ** i)):
            flag_left = True
        else:
            return False
    for j in range(1, len(str(n))):
        if is_prime(int(n / 10 ** j)):
            flag_right = True
        else:
            return False
    if flag_right and flag_left:
        return True
    return False
def is_pandigital(n):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digit in str(n):
        if digit in numbers:
            numbers.remove(digit)
        else:
            return False
        if not numbers:
            return True
def ways_to_make_right_triangle(perimeter):
    ways = 0
    for b in range(1, int(perimeter / 2)):
        for c in range(1, (perimeter / 2)):
            if (((b ** 2) + (c ** 2)) ** 0.5) + b + c == perimeter:
                ways += 1

    # for a in range(1, perimeter):
    #     for b in range(1, perimeter - a):
    #         for c in range(1, perimeter - a - b):
    #             if (a ** 2 == (b ** 2) + (c ** 2)) and (a + b + c == perimeter):
    #                 ways += 1
    return ways
def is_triangle(n):
    step = 1
    _sum = 0
    while _sum <= n:
        if _sum == n:
            return True
        _sum += step
        step += 1
    return False


def get_word_value(word):
    value = 0
    for letter in word:
        value += ord(letter) - 64
    return value
def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()
def get_triangle_number(n):
    return (n * (n + 1)) / 2


def get_pentagonal_number(n):
    return (n * (3 * n - 1)) / 2


def get_hexagonal_number(n):
    return n * (2 * n - 1)
def goldbach(n):
    primes = get_all_primes_until(n)
    flag = False
    for prime in primes:
        q = (n - prime) / 2
        if str(q ** 0.5).split('.', 1)[1] == '0':     # bitches im smart
            flag = True

    return flag
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors
def self_powers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum
def is_permutation(a, b):
    if a != b and len(str(a)) == len(str(b)):
        digits = []
        for digit in str(a):
            digits.append(digit)
        for digit in str(b):
            if digit in digits:
                digits.remove(digit)
            else:
                return False
        return True
    return False
def select_r_from_n(r, n):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
def analyze_poker_hand(hand):
    h = ''.join(i for i in hand)
    ranking = [0] * 7
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cards_per_rank = [0] * 13

    for rank in card_ranks:
        cards_per_rank[card_ranks.index(rank)] = h.count(rank)
    m = max(cards_per_rank)
    temp_i = 2
    for i in range(12, -1, -1):
        if cards_per_rank[i] >= 1:
            ranking[temp_i] = i
            temp_i += 1

    if m == 1:
        if ranking[2] - ranking[6] == 4:
            ranking[0] = 4  # Straight

    elif m == 2:
        if cards_per_rank.count(2) == 2:
            ranking[0] = 2  # 2 pairs
            temp_i = 1
            for i in range(12, -1, -1):
                if cards_per_rank[i] == 2:
                    ranking[temp_i] = i
                    temp_i += 1
                elif cards_per_rank[i] == 1:
                    ranking[3] = i
        else:
            ranking[0] = 1  # 1 pair
            ranking[1] = cards_per_rank.index(2)
    elif m == 3:
        if 2 in cards_per_rank:
            ranking[0] = 6  # full house
            ranking[1] = cards_per_rank.index(3)
        else:
            ranking[0] = 3  # 3 of a kind
            ranking[1] = cards_per_rank.index(3)
    elif m == 4:
        ranking[0] = 7  # 4 of a kind
        ranking[1] = cards_per_rank.index(4)

    if h.count('H') == 5 or h.count('D') == 5 or h.count('S') == 5 or h.count('C') == 5:
        if h.count('A') == 1 and h.count('K') == 1 and h.count('Q') == 1 and h.count('J') == 1 and h.count('T') == 1:
            ranking[0] = 9  # GG Royal flush
        elif ranking[2] - ranking[6] == 4:
            ranking[0] = 8  # Straight flush
        else:
            ranking[0] = 5  # Flush
    return ranking


def compare_poker_hands(hand1, hand2):
    hand1_ranking = analyze_poker_hand(hand1)
    hand2_ranking = analyze_poker_hand(hand2)

    for i in range(len(hand1_ranking)):
        if hand1_ranking[i] > hand2_ranking[i]:
            return 1
        elif hand1_ranking[i] < hand2_ranking[i]:
            return 2
        else:
            continue
    return 0
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
def get_all_primes_until(n):
    primes = [1, 2]
    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def sieve_of_eratosthenes(n):
    """

    :param n: until n
    :return: returns both the array of primes and the boolean table
    """
    a = [True] * (n + 1)
    i = 2
    while i <= n ** 0.5:
        if a[i]:
            j = i * i

            while j <= n:
                a[j] = False
                j += i
        i += 1

    r = []
    for idx in range(1, n + 1):
        if a[idx]:
            r.append(idx)
    return r , a






def phi_function(n):
    result = n
    primes = prime_factors(n)
    for prime in primes:
        t = 1 - 1 / prime
        result *= t
    return result
def matrix_to_triangle(matrix):       # make a filler shadow to make a triangle form
    triangle = [[] for i in range(2 * len(matrix) - 1)]
    filler = max(max(matrix)) + 1
    for j in range(2 * len(matrix) - 1):
        for i in range(2 * len(matrix) - 1 - j):
            if i >= len(matrix) or j >= len(matrix):
                triangle[i + j].append(filler)
            else:
                triangle[i + j].append(matrix[i][j])
    return triangle


# From euler18 max_sum_path
def min_sum_path(triangle):
    row_idx = len(triangle) - 2
    for row in reversed(triangle[:(len(triangle) - 1)]):
        for i in range(len(row)):
            row[i] = row[i] + min([triangle[row_idx + 1][i], triangle[row_idx + 1][i + 1]])
            triangle[row_idx][i] = row[i]
        row_idx = row_idx - 1
    return triangle[0][0]
def number_chain_loop_point(n):
    while True:
        m = 0
        for d in str(n):
            m += int(d) ** 2
        n = m
        if n == 1 or n == 89:
            break
    return n
def red_ways(tiles):
    s = 0
    for i in range(1, (tiles // 2) + 1):
        s += choose(tiles - i, i)
    return s


def green_ways(tiles):
    s = 0
    for i in range(1, (tiles // 3) + 1):
        s += choose(tiles - (2 * i), i)
    return s


def blue_ways(tiles):
    s = 0
    for i in range(1, (tiles // 4) + 1):
        s += choose(tiles - (i * 3), i)
    return s
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
def set_of_nums(goal, n, min, max):
    range_ = range(min, max + 1)
    r = []
    for i in itertools.product(range_, repeat=n):
        if sum(i) == goal:
            r.append(i)
    return r


def choose(n, k):
    if n < k:
        return 0
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def generate_continued_fraction_of_e(n):
    seq = [1, 2]
    idx = 2
    jumper = 0
    while idx < n:
        idx += 1
        if jumper == 2:
            seq.append(seq[idx - 4] + 2)
            jumper = 0
        else:
            seq.append(1)
            jumper += 1
    return seq


def get_convergent_fraction(s, sequence):
    n = 1
    d = sequence[s - 2]
    paidx = s - 3
    pa = sequence[paidx]
    steps = 1
    while steps <= s - 2:
        new_n = pa * d
        n = new_n + n
        temp = d
        d = n
        n = temp
        paidx -= 1
        pa = sequence[paidx]
        steps += 1
    return n + (2 * d), d