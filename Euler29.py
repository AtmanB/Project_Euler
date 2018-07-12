# https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

def main():
    ans = distinct_powers(100, 100)
    ans.sort()
    print(len(ans))

def distinct_powers(a, b):
    powers = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            powers.append(i ** j)

    return list(set(powers))
main()