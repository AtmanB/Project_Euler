from Timer import timethis
# main 1.4080803394317627

@timethis
def main(percentage):
    slopes = create_slopes()
    buffer1 = []
    buffer2 = []
    digits = 3
    bouncy = 0
    total = 99
    ans = 0
    reached_percentage = False

    # creating buffer1, examining all 3 digit numbers
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                exam = slopes[i][j] | slopes[j][k]
                buffer1.append(exam)

                total += 1
                if exam == 3:
                    bouncy += 1

                if ((bouncy / total) * 100) == percentage and not reached_percentage:
                    ans = total
                    reached_percentage = True

    while not reached_percentage:
        if digits % 2 == 1:
            for i in range(len(buffer1)):
                for j in range(10):
                    exam = buffer1[i] | slopes[i % 10][j]
                    buffer2.append(exam)
                    total += 1

                    if exam == 3:
                        bouncy += 1

                    if ((bouncy / total) * 100) == percentage and not reached_percentage:
                        ans = total
                        reached_percentage = True
                        return ans
            digits += 1
            buffer1.clear()

        else:
            for i in range(len(buffer2)):
                for j in range(10):
                    exam = buffer2[i] | slopes[i % 10][j]
                    buffer1.append(exam)
                    total += 1

                    if exam == 3:
                        bouncy += 1

                    if ((bouncy / total) * 100) == percentage and not reached_percentage:
                        ans = total
                        reached_percentage = True
                        return ans
            digits += 1
            buffer2.clear()



def create_slopes():
    slopes = []

    for i in range(10):
        temp = []
        for j in range(10):
            if j < i:
                temp.append(2)
            elif j == i:
                temp.append(0)
            else:
                temp.append(1)
        slopes.append(temp)
    return slopes


if __name__ == '__main__':
    ans = main(99)
    print(ans)
