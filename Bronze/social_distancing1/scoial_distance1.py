#"""Returns size of largest gap between two 1s and also the index where it starts"""
largest_gap_start = -1


def copy_list(old_list):
    new_list = []
    for item in old_list:
        new_list.append(item)
    return new_list


def find_largest_interior_gap(stall_list):
    biggest_gap = 0
    current_start = -1  # if there is no 1, current_start will remain to be -1
    list_length = len(stall_list)

    for i in range(0, list_length):
        if stall_list[i] == "1":
            if current_start != -1 and i - current_start > biggest_gap:
                biggest_gap = i - current_start
                global largest_gap_start
                largest_gap_start = current_start

            current_start = i

    return biggest_gap


#'''Returns size of smallest gap between two 1s'''


def find_smallest_interior_gap(stall_list):
    smallest_gap = len(stall_list)
    current_start = -1
    list_length = len(stall_list)
    for i in range(0, list_length):
        if stall_list[i] == "1":
            if current_start != -1 and i - current_start < smallest_gap:
                smallest_gap = i - current_start
            current_start = i
    return smallest_gap


def try_cow_in_largest_gap(stall_list):
    global largest_gap_start
    largest_gap = find_largest_interior_gap(stall_list)
    #'''evenly divide the largest gap'''
    if largest_gap >= 2:
        stall_list[int(largest_gap_start + largest_gap / 2)] = "1"
        return find_smallest_interior_gap(stall_list)
    return -1  # no gap


with open("socdist1.in", "r") as input_file:
    stall_num = int(input_file.readline())
    current_stall = []
    for i in range(0, stall_num):
        #''' read(1) means read one character'''
        current_stall.append(input_file.read(1))

    answer = 0
    #'''Possibility 1. put two cows in largest interior gap'''
    largest_gap = find_largest_interior_gap(current_stall)
    if largest_gap >= 3:
        temp = copy_list(current_stall)
        temp[int(largest_gap_start + largest_gap / 3)] = "1"
        temp[int(largest_gap_start + largest_gap * 2 / 3)] = "1"
        answer = max(answer, find_smallest_interior_gap(temp))

    #'''Possibility 2. cows at both ends'''
    if current_stall[0] == "0" and current_stall[stall_num - 1] == "0":
        temp = copy_list(current_stall)
        temp[0] = "1"
        temp[stall_num - 1] = "1"
        answer = max(answer, find_smallest_interior_gap(temp))

    #'''Possibility 3. cow at left + cow in largest interior gap'''
    if current_stall[0] == "0":
        temp = copy_list(current_stall)
        temp[0] = "1"
        answer = max(answer, try_cow_in_largest_gap(temp))

    #'''Possibility 4. cow at right + cow in largest interior gap'''
    if current_stall[stall_num - 1] == "0":
        temp = copy_list(current_stall)
        temp[stall_num - 1] = "1"
        answer = max(answer, try_cow_in_largest_gap(temp))

    #'''Possibility 5. cow at largest interior gap.  done twice'''
    if largest_gap >= 2:
        temp = copy_list(current_stall)
        temp[int(largest_gap_start + largest_gap / 2)] = "1"
        answer = max(answer, try_cow_in_largest_gap(temp))

    with open("socdist1.out", "w") as output_file:
        output_file.write(str(answer))
