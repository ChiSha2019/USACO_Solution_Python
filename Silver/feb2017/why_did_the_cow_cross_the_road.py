from bisect import bisect_right
class Cow:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __gt__(self, other):
        return other.__lt__(self)

with open("5.in", "r") as input_file:
    list1 = input_file.readline().split()
    C = int(list1[0])
    N = int(list1[1])
    list_t_chick = []
    for i in range(C):
        list_t_chick.append(int(input_file.readline()))
    list_cow = []
    cow_visited = [False]*N
    for i in range(N):
        list2 = input_file.readline().split()
        list_cow.append(Cow(int(list2[0]), int(list2[1])))

    list_t_chick.sort()
    list_cow.sort()
    count = 0

    #have to use binary search
    '''for cow in list_cow:
        for i in range(C):
            if cow.start <= list_t_chick[i] <= cow.end:
                count += 1
                list_t_chick.pop(i)
                print(i)
                C -= 1
                break'''

    for cow in list_cow:
        i = bisect_right(list_t_chick, cow.start)
        if i != len(list_t_chick) and cow.start <= list_t_chick[i] <= cow.end:
            count += 1
            list_t_chick.pop(i)

    with open("helpcross.out", "w") as output_file:
        output_file.write(str(count))




'''
    #brute force
    for i in range(C):
        for j in range(i, N):
            if (not cow_visited[j]) and list_cow[j].start <= list_t_chick[i] <= list_cow[j].end:
                count += 1
                cow_visited[j] = True
                break
'''
