from Timer import timethis


@timethis
def main():
    logins = [319,
              680,
              180,
              690,
              129,
              620,
              762,
              689,
              762,
              318,
              368,
              710,
              720,
              710,
              629,
              168,
              160,
              689,
              716,
              731,
              736,
              729,
              316,
              729,
              729,
              710,
              769,
              290,
              719,
              680,
              318,
              389,
              162,
              289,
              162,
              718,
              729,
              319,
              790,
              680,
              890,
              362,
              319,
              760,
              316,
              729,
              380,
              319,
              728,
              716]

    for passcode in range(60000000, 70000000):
        for login in logins:
            if str(login)[0] in str(passcode) and str(login)[1] in str(passcode) and str(login)[2] in str(passcode):
                if str(passcode).index(str(login)[0]) < str(passcode).index(str(login)[1]) and str(passcode).index(str(login)[1]) < str(passcode).index(str(login)[2]):
                    if len(logins) - 1 == logins.index(login):
                        print(passcode)
                    continue
                else:
                    break



if __name__ == '__main__':
    main()