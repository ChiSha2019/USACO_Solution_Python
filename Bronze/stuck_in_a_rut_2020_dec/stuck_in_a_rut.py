with open("1.in", "r") as input_file:
    N = int(input_file.readline())
    cows =[]
    for i in range(N):
        each_line = []
        each_line1 = input_file.readline().split()
        #convert each line into "string" "int" "int"
        each_line.append(each_line1[0])
        each_line.append(int(each_line1[1]))
        each_line.append(int(each_line1[2]))
        cows.append(each_line)

    '''construct a 2D array with index cow_num, cow_num, value to be time'''
    max_colliding_time = 0
    collision_array = [[0]*N for _ in range(N)] #row cow collides with column cow
    for i in range(0, N-1):
        for j in range(i+1,N):
            '''cow i hits cow j'''
            if cows[i][0] == 'N' and cows[j][0] == 'E' and cows[i][1] >= cows[j][1] and cows[i][2] <= cows[j][2] \
                    or (cows[i][0] == 'E' and cows[i][1] <= cows[j][1] and cows[i][2] >= cows[j][2]) :
                collision_array




    print(cows)