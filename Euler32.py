def main():
    products = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    flag = True
    for i in range(1, 9877):
        for j in range(i, int(9877 / i)):
            k = i * j
            if len(str(k) + str(i) + str(j)) == 9:

                for number in str(k):
                    if number in numbers:
                        numbers.remove(number)
                    else:
                        flag = False
                for number in str(i):
                    if number in numbers:
                        numbers.remove(number)
                    else:
                        flag = False
                for number in str(j):
                    if number in numbers:
                        numbers.remove(number)
                    else:
                        flag = False
                if numbers == [] and flag:
                    products.append(k)
                numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                flag = True
    lol = set(products)
    print(sum(lol))


if __name__ == '__main__':
    main()

