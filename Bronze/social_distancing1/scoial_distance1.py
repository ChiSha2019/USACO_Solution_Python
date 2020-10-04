#like cutting rope?
with open("1.in", "r") as input_file:
    stall_num = int(input_file.readline())
    current_stall = input_file.readline()
    min_distance = stall_num
    stall_distance_list = []
    previous_1_index = -1
    for i in range(0, len(current_stall)):
        if current_stall[i] == "1":
            stall_distance_list.append(i - previous_1_index)
            previous_1_index = i
            if i - previous_1_index < min_distance:
                min_distance = i - previous_1_index

                

    stall_distance_list.append(stall_num - previous_1_index)
    print(stall_distance_list)
