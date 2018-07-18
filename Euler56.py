# piece of cake, lol


def main():
    ans = 0
    for a in range(2,101):
        for b in range(2, 101):
            googol = a ** b
            googol_sum = 0
            for d in str(googol):
                googol_sum += int(d)
            if googol_sum > ans:
                ans = googol_sum
    print(ans)



if __name__ == '__main__':
    main()