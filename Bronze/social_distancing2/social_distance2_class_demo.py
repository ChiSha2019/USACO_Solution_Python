'''
1. find max R = smallest distance between healthy and a sick cow
2. use R to determine independent blocks of sick cow
    a) determine the number of sick blocks (endpoint with 1 no -1 inside)
    b) determine number subblocks inside with doistance > r
     <=> find number of gaps > R
3. number of independent blocks is the number of initial sick cow
'''
def find_smallest_01_gap(A):
    smallest_gap = len(A)
    current_start = -1
    for i in range(0, 1000001):
        if A[i] != 0:
            if current_start != -1 and A[current_start] != A[i] and i - current_start<smallest_gap:
                smallest_gap = i - current_start
            current_start = i
    return smallest_gap

def num_sick_clusters(A):
    last_state = 0
    num_cluster = 0
    for i in range(0, 1000001):
        if A[i] != 0:
            if A[i] != last_state and A[i] == 1: # find the start of a new block
                num_cluster += 1
            last_state = A[i]
    return num_cluster

def num_sick_gap(A, r):
    answer = 0
    current_start = 0
    for i in range(0, 1000001):
        if A[i] != 0:
            if current_start != 0 and A[current_start] == 1 and A[i] == 1 and i-current_start>=r:
                answer += 1
            current_start = i
    return answer


with open("socdist2.in", "r") as input_file:
    N = int(input_file.readline())
    A = list()
    for i in range(0, 1000001):
        A.append(0)

    for i in range(0,N):
        line = input_file.readline().split()
        if line[1] == "1":
            A[int(line[0])] = 1
        else:
            A[int(line[0])] = -1 #healthy cow

    with open("socdist2.out", "w") as output_file:
        r = find_smallest_01_gap(A)
        output_file.write(str(num_sick_clusters(A) + num_sick_gap(A,r)))
