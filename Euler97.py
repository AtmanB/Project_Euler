from Timer import timethis
# 496 seconds... really slow... needs some thinking

@timethis
def main():
    ans = str((28433 * (2 ** 7830457)) + 1)[-10:]
    print(ans)

main()