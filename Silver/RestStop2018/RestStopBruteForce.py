with open("reststops.in", "r") as input_file:
    line1 = input_file.readline().split()
    length = int(line1[0])
    stops = int(line1[1])
    ratef = int(line1[2])
    rateb = int(line1[3])
    stop_list = []
    for i in range(stops):
        line = input_file.readline().split()
        stop_list.append((int(line[0]),(int(line[1]))))

    bessiepos = 0
    tastypoints = 0

    while True:
        maximum = (0, 0)
        for x in stop_list:
            if x[0] > bessiepos and x[1] >= maximum[1]:
                maximum = x
        tastypoints += (maximum[0] - bessiepos) * (ratef - rateb) * maximum[1]
        bessiepos = maximum[0]
        if bessiepos == stop_list[-1][0]:
            break

    with open("reststops.out", "w") as output_file:
        output_file.write(str(tastypoints))