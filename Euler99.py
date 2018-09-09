from math import log10

from Timer import timethis


@timethis
def main():
    bases = []
    exponents = []
    with open('p099_base_exp.txt') as data:
        for line in data:
            bases.append(line.split(',')[0])
            exponents.append(line.split(',')[1])

    for i in range(len(bases)):
        bases[i] = log10(int(bases[i]))
    for i in range(len(exponents)):
        exponents[i] = bases[i] * int(exponents[i])
    m = max(exponents)
    print(exponents.index(m) + 1)


if __name__ == '__main__':
    main()
