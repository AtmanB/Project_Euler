from Timer import timethis


@timethis
def main():
    m = []
    # print(matrix_to_triangle(m))

    with open('p081_matrix.txt') as txt:
        for line in txt:
            casting = line[:-1].split(',')
            casting = [int(i) for i in casting]
            m.append(casting)

    tri_m = matrix_to_triangle(m)
    print(min_sum_path(tri_m))


def matrix_to_triangle(matrix):       # make a filler shadow to make a triangle form
    triangle = [[] for i in range(2 * len(matrix) - 1)]
    filler = max(max(matrix)) + 1
    for j in range(2 * len(matrix) - 1):
        for i in range(2 * len(matrix) - 1 - j):
            if i >= len(matrix) or j >= len(matrix):
                triangle[i + j].append(filler)
            else:
                triangle[i + j].append(matrix[i][j])
    return triangle


# From euler18 max_sum_path
def min_sum_path(triangle):
    row_idx = len(triangle) - 2
    for row in reversed(triangle[:(len(triangle) - 1)]):
        for i in range(len(row)):
            row[i] = row[i] + min([triangle[row_idx + 1][i], triangle[row_idx + 1][i + 1]])
            triangle[row_idx][i] = row[i]
        row_idx = row_idx - 1
    return triangle[0][0]


if __name__ == '__main__':
    main()
