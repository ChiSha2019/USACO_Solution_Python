def is_right_triangle(x1, x2, x3, y1, y2, y3) -> bool:
    return x1 == x2 and y2 == y3 or \
           x1 == x2 and y1 == y3 or \
           x2 == x3 and y1 == y3 or \
           x2 == x3 and y1 == y2 or \
           x1 == x3 and y3 == y2


with open("1.in", "r") as input_file:
    coordinate_number = int(input_file.readline())
    coordinate_list = []
    for i in range(0, coordinate_number):
        line_int = list(map(int, input_file.readline().split()))
        coordinate_list.append(line_int)
    max_area = 0

    for i in range(0, len(coordinate_list)):
        for j in range(i + 1, len(coordinate_list)):
            for k in range(j + 1, len(coordinate_list)):
                x1 = coordinate_list[i][0]
                y1 = coordinate_list[i][1]
                x2 = coordinate_list[j][0]
                y2 = coordinate_list[j][1]
                x3 = coordinate_list[k][0]
                y3 = coordinate_list[k][1]
                #another approach is to break condition into specific cases
                if is_right_triangle(x1, x2, x3, y1, y2, y3):
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    if area > max_area:
                        max_area = area

    print(max_area)
