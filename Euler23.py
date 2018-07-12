from Euler21 import proper_divisor_sum

#  A BIT SLOW, BUT HEY IT WORKS... OK ITS VERY SLOW... #PYTHON_NOOB

def main():
    abuns = get_abundant_numbers(28124)
    r = list(range(1, 28124))
    combos = abundant_number_combos(abuns)
    for number in combos:
        r.remove(number)
    ans = 0
    for n in r:
        ans = ans + n
    print(ans)


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



main()
