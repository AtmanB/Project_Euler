# https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string

def main():
    big_ans = str(self_powers(1000))
    print(big_ans[-10:])



def self_powers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum

main()
