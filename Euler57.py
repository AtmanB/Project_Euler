# 2 fores proigoumeno denominator + diafora proigoumenou denominator me numenator
from Timer import timethis


@timethis
def main():
    numerators = [3] + [0] * 999
    denominators = [2] + [0] * 999
    ans = 0
    for i in range(1, 1000):
        denominators[i] = (denominators[i - 1] * 2) + (numerators[i - 1] - denominators[i - 1])
        numerators[i] = denominators[i] + denominators[i - 1]
        if len(str(numerators[i])) > len(str(denominators[i])):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
