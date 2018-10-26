def main(n):

    global finishers
    global zones

    total = 21
    finishers = [0] * 21
    zones = [0] * 62
    for i in range(20):
        finishers[i] = (i+1)*2
    finishers[-1] = 50

    for i in range(3):
        for j in range(20):
            zones[i*20 + j] = (j + 1) * (i + 1)
    zones[-2], zones[-1] = 25, 50

    total += two_darts(n)
    total += three_darts(n)

    return total



def two_darts(n):
    t = 0
    for i in range(62):
        for f in range(21):
            check = zones[i] + finishers[f]
            if check < n:
                t += 1
    return t

def three_darts(n):
    t = 0
    for i in range(62):
        for j in range(i, 62):
            for f in range(21):
                check = zones[i] + zones[j] + finishers[f]
                if check < n:
                    t += 1
    return t

if __name__ == '__main__':
    print(main(100))

'''
possible_throws = sorted(range(20+1) + [2*n for n in range(1, 20+1)] + [3*n for n in range(1, 20+1)] + [25, 50])
count = 0
possible_doubles = [2*n for n in range(1, 20+1)] + [50]
for i in range(len(possible_throws)):
    for j in range(i+1):
        for dart3 in possible_doubles:
            if possible_throws[i] + possible_throws[j] + dart3 < 100:
                count += 1

print count
'''