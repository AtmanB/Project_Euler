def main():
    triangles = []
    with open('p102_triangles.txt') as file:
        for line in file:
            cast = line[:-1].split(',')
            triangles.append([int(i) for i in cast])
    ans = 0
    for triangle in triangles:
        print(triangle)
        if includes_origin(triangle):
            ans += 1
    print(triangles[9])
    if includes_origin(triangles[9]):
        print('yay!')
    print('Answer = ', ans)


def opposite_signs_zero(a, b):
    v = sorted([a, b])
    if v[0] <= 0 <= v[1]:
        return True
    else:
        return False


def get_line_equation(x1, y1, x2, y2):
    if x2 != x1:

        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
    else:
        a = 0
        b = x1
    return a, b


def includes_origin(t):
    axises = []
    # testing AB
    if opposite_signs_zero(t[0],t[2]) and opposite_signs_zero(t[1],t[3]):
        a, b = get_line_equation(t[0], t[1], t[2], t[3])
        if b > 0:
            axises.append(2)
        elif b < 0:
            axises.append(4)
        else:
            return False
        if a != 0:
            if b / a < 0:
                axises.append(1)
            else:
                axises.append(3)

    elif opposite_signs_zero(t[0],t[2]) and t[1] > 0:
        axises.append(2)
    elif opposite_signs_zero(t[0],t[2]) and t[1] < 0:
        axises.append(4)
    elif opposite_signs_zero(t[1],t[3]) and t[0] > 0:
        axises.append(1)
    elif opposite_signs_zero(t[1],t[3]) and t[0] < 0:
        axises.append(3)

    # testing BC
    if opposite_signs_zero(t[2],t[4]) and opposite_signs_zero(t[3],t[5]):
        a, b = get_line_equation(t[2], t[3], t[4], t[5])
        if b > 0:
            axises.append(2)
        elif b < 0:
            axises.append(4)
        else:
            return False
        if a != 0:
            if b / a < 0:
                axises.append(1)
            else:
                axises.append(3)
    elif opposite_signs_zero(t[2],t[4]) and t[3] > 0:
        axises.append(2)
    elif opposite_signs_zero(t[2],t[4]) and t[3] < 0:
        axises.append(4)
    elif opposite_signs_zero(t[3],t[5]) and t[2] > 0:
        axises.append(1)
    elif opposite_signs_zero(t[3],t[5]) and t[2] < 0:
        axises.append(3)

        # testing AC
    if opposite_signs_zero(t[0],t[4]) and opposite_signs_zero(t[1],t[5]):
        a, b = get_line_equation(t[0], t[1], t[4], t[5])
        if b > 0:
            axises.append(2)
        elif b < 0:
            axises.append(4)
        else:
            return False
        if a != 0:
            if b / a < 0:
                axises.append(1)
            else:
                axises.append(3)
    elif opposite_signs_zero(t[0],t[4]) and t[1] > 0:
        axises.append(2)
    elif opposite_signs_zero(t[0],t[4]) and t[1] < 0:
        axises.append(4)
    elif opposite_signs_zero(t[1],t[5]) and t[0] > 0:
        axises.append(1)
    elif opposite_signs_zero(t[1],t[5]) and t[0] < 0:
        axises.append(3)
    print(axises)
    if 1 in axises and 2 in axises and 3 in axises and 4 in axises:
        return True
    else:
        return False
# def quads(triangle):
#     quads = []
#     q = 0
#     for i, j in [(0,1),(2,3),(4,5)]:
#         print(i,j)
#         if triangle[i] > 0 and triangle[j] > 0:
#             quads.append(2)
#         elif triangle[i] < 0 and triangle[j] > 0:
#             quads.append(0)
#         elif triangle[i] < 0 and triangle[j] < 0:
#             quads.append(-2)
#         elif triangle[i] > 0 and triangle[j] < 0:
#             quads.append(0)
#         elif triangle[i] == 0 and triangle[j] > 0:
#             quads.append(12)
#         elif triangle[i] == 0 and triangle[j] < 0:
#             quads.append(34)
#         elif triangle[i] < 0 and triangle[j] == 0:
#             quads.append(23)
#         elif triangle[i] > 0 and triangle[j] == 0:
#             quads.append(41)
#         elif triangle[i] == triangle[j] == 0:
#             return False



if __name__ == '__main__':
    main()