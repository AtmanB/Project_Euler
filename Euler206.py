#  3003 secs, needs revision

import fnmatch

from Timer import timethis


@timethis
def main():
    TARGET = '1?2?3?4?5?6?7?8?9?0'
    for n in range(1000000000, 1400000000):
        if fnmatch.fnmatch(str(n ** 2), TARGET):
            print(n)
            break


if __name__ == '__main__':
    main()