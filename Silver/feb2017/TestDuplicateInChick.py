with open("9.in", "r") as input_file:
    list1 = input_file.readline().split()
    C = int(list1[0])
    N = int(list1[1])
    set_t_chick = set()
    for i in range(C):
        t = int(input_file.readline())
        if t in set_t_chick:
            print("duplicate is " + str(t))
            break
        else:
            set_t_chick.add(int(input_file.readline()))
