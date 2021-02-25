from bisect import bisect_left
from bisect import bisect_right
class Cow:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.end == other.end:
            return self.start > other.start
        return self.end < other.end

    def __gt__(self, other):
        return other.__lt__(self)

with open("helpcross.in","r") as input_f:
    list1 = input_f.readline().split()
    C = int(list1[0])
    N = int(list1[1])
    list_chick = []
    for i in range(C):
        list_chick.append(int(input_f.readline()))
    list_cow = []
    for i in range(N):
        list2 = input_f.readline().split()
        list_cow.append(Cow(int(list2[0]), int(list2[1])))

    list_chick.sort() #clogc
    list_cow.sort() #nlog(n)
    count = 0
    cow_visted = [False] * N

    for cow in list_cow:
        i = bisect_left(list_chick, cow.start)
        if i < len(list_chick) and list_chick[i] <= cow.end:
            count += 1
            list_chick.pop(i)

    with open("helpcross.out","w") as output_f:
        output_f.write(str(count))
