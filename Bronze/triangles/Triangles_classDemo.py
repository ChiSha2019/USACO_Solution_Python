'''
1.exhaustive search every three coordinate pairs and check whether they can
form a valid right triangle
(0,0)(0,1)(1,0)
(0,0)(0,1)(1,2)
(0,0)(1,0)(1,2)
(0,1)(1,0)(1,2)

2.If it's valid, calculate it's area and find the maximum area
'''
def is_right_triangle(x1,x2,x3,y1,y2,y3) -> bool:
    return (x1 == x2 or x1 == x3 or x2 == x3) and \
           (y1 == y2 or y1 == y3 or y2 == y3)
    '''
    return x1 == x2 and y2 == y3 or \
           x1 == x3 and y2 == y3 or \
           x2 == x3 and y1 == y3 or \
           x2 == x3 and y1 == y2 or \
           x1 == x2 and y1 == y2 or \
           x1 == x3 and y1 == y2 or \
           x1 == x2 and y1 == y3 or \
           
           '''

with open("triangles.in", 'r') as input_file:
    num_coordinates = int(input_file.readline())
    coordinate_list = []
    for i in range(0, num_coordinates):
        line_int = list(map(int, input_file.readline().split()))
        coordinate_list.append(line_int)

    max_area = 0
    for i in range(0, num_coordinates - 2):
        for j in range(i + 1, num_coordinates - 1):
            for k in range(j + 1, num_coordinates):
                x1 = coordinate_list[i][0]
                y1 = coordinate_list[i][1]
                x2 = coordinate_list[j][0]
                y2 = coordinate_list[j][1]
                x3 = coordinate_list[k][0]
                y3 = coordinate_list[k][1]

                if is_right_triangle(x1,x2,x3,y1,y2,y3):
                    #https://www.mathopenref.com/coordtrianglearea.html
                    area = abs(x1*(y2 - y3) + x2*(y3-y1)+x3*(y1-y2))
                    if area > max_area:
                        max_area = area
                        print(str(x1)+ " " + str(y1)
                              + ", " + str(x2) + " "+ str(y2)+
                              "," +str(x3) + " "+str(y3))

    with open("triangles.out", "w") as output_file:
        output_file.write(str(max_area))


