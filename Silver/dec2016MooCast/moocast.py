'''
def dfs(curr):
    if isVisted[curr]:
        return 0
    else:
        isVisted[curr] = True
        num = 1
        for i in range(N):

with open("1.in", "r") as input_file:
     N = int(input_file.readline())
    x = []
    y = []
    r = []
    for i in range(N):
        listcow = input_file.readline().split()
        x.append(listcow[0])
        y.append(listcow[1])
        r.append(listcow[2])

    canTransmit = [[False]*N]*N #n by n array
    for i in range(N):
        for j in range(N):
            square_dist = (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            if square_dist <= r[i]*r[i]:
                canTransmit[i][j] = True

    global isVisted = []
    global numCanHear = 1 #the bradcaster itself
    for i in range(N):
        isVisted = [False]*N
        numCanHear = max(numCanHear, dfs(i))

    print(numCanHear)

'''



