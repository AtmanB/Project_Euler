from Timer import timethis


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




@timethis
def main():
    # print(generate_continued_fraction_of_e(10))
    seq = generate_continued_fraction_of_e(99)
    n , d = get_convergent_fraction(100, seq)
    print(n, d)
    ans = 0
    for d in str(n):
        ans += int(d)
    print(ans)

if __name__ == '__main__':
    main()