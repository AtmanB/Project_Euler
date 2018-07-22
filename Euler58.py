from Euler27 import is_prime
from Timer import timethis


@timethis
def main():
    current = 9
    prime_counter = 3
    counter = 5
    h = 3
    while (prime_counter * 100) / counter >= 10:
        h += 2
        for i in range(4):
            current += h - 1
            if is_prime(current):
                prime_counter += 1
            counter += 1
    print(h)


if __name__ == '__main__':
    main()