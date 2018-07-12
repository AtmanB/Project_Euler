# https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python

import itertools

ans = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(str(ans[999999]).replace(' ', '').replace(',', '').replace('(', '').replace(')', ''))
