def hungarian_max(m):
    l = len(m)
    m0 = []
    for row in m:
        temp = []
        max_ = max(row)
        for i in row:
            temp.append(max_ - i)
        m0.append(temp)
    flags = [True if column(m0, i).count(0) == 1 else False for i in range(l)]
    indexes = [row.index(0) for row in m0]
    if not False in flags:
        return sum([m[i][indexes[i]] for i in range(l)])


    marked_columns = []
    true_rows = []
    print(flags, indexes)
    while len(marked_columns) + len(true_rows) != l:
        # marked_columns = []
        marked_rows = [i for i in range(l)]

        zeroes = []
        for i in range(l):
            for j in range(l):
                if m0[i][j] == 0:
                    zeroes.append([i, j])
        all_zeroes = zeroes.copy()

        for zero in zeroes:
            del_r = zero[0]
            del_c = zero[1]
            for zero2 in zeroes[zeroes.index(zero) + 1:]:
                if del_r == zero2[0] or del_c == zero2[1]:
                    zeroes.remove(zero2)
            print(zeroes)
        print(zeroes, all_zeroes)
        for zero in zeroes:
            if zero[0] in marked_rows:
                marked_rows.remove(zero[0])
        for r in marked_rows:
            for z in all_zeroes:
                if r == z[0]:
                    if z[1] not in marked_columns:
                        marked_columns.append(z[1])
        for c in marked_columns:
            for z in zeroes:
                if c == z[1]:
                    if z[0] not in marked_rows:
                        marked_rows.append(z[0])
        marked_rows = sorted(marked_rows)
        marked_columns = sorted(marked_columns)
        print(marked_rows, marked_columns)
        elements_left = []
        true_columns = [i for i in range(l) if i not in marked_columns]
        true_rows = [i for i in range(l) if i not in marked_rows]
        for i in marked_rows:
            for j in true_columns:
                elements_left.append(m0[i][j])
        print(elements_left)
        min_ = min(elements_left)
        for i in marked_rows:
            for j in true_columns:
                m0[i][j] -= min_
        for i in true_rows:
            for j in marked_columns:
                m0[i][j] += min_
    print(m, m0)






def column(matrix, i):
    return [row[i] for row in matrix]


def main(m):
    ans = hungarian_max(m)
    print(ans)


if __name__ == '__main__':
    matrix = [[7, 53, 183, 439, 863],
         [497, 383, 563, 79, 973],
         [287, 63, 343, 169, 583],
         [627, 343, 773, 959, 943],
         [767, 473, 103, 699, 303]]
    test = [[1,2,3], [4,6,5], [9,8,7]]
    main(matrix)
