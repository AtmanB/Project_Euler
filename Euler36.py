def main():
    # https: // stackoverflow.com / questions / 699866 / python - int - to - binary
    ans = 0
    for n in range(1,1000000):
        if str(n) == str(n)[::-1]:
            n_binary = format(n, 'b')
            if str(n_binary) == str(n_binary)[::-1]:
                ans += n
            print(n)
    print(ans)
main()
