with open("photo.in", "r") as input_file:
    cow_num = int(input_file.readline())
    b_list = input_file.readline().split()
    b_list = list(map(int, b_list))
    a_list = []
    a_set = set()

    for i in range(1, cow_num + 1):
        isGood = True
        a_list.append(i)
        a_set.add(i)
        for item in b_list:
            nextItemInA = item - a_list[-1]
            if nextItemInA > cow_num or nextItemInA <= 0 or nextItemInA in a_set:
                a_list.clear()
                a_set.clear()
                isGood = False
                break
            else:
                a_list.append(nextItemInA)
                a_set.add(nextItemInA)

        if isGood:
            with open("photo.out", "w") as output_file:
                for i in range(0, len(a_list)):
                    output_file.write(str(a_list[i]))
                    if i < len(a_list) -1:
                        output_file.write(" ")
