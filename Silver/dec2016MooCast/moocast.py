isVisted = []

def dfs(curr):
    if isVisted[curr]:
        return 0
    else:
        isVisted[curr] = True
        num = 1
        for i in range(N):
            if canTransmit[curr][i]:
                num += dfs(i)
        return num

with open("moocast.in", "r") as input_file:
    N = int(input_file.readline())
    x = []
    y = []
    r = []
    for i in range(N):
        listcow = input_file.readline().split()
        x.append(int(listcow[0]))
        y.append(int(listcow[1]))
        r.append(int(listcow[2]))

    global canTransmit
    #canTransmit = [[False]*N]*N #n by n array
    canTransmit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            square_dist = (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            canTransmit[i][j] = (square_dist <= r[i]*r[i])

    numCanHear = 1 #the bradcaster itself
    for i in range(N):
        isVisted = [False]*N
        numCanHear = max(numCanHear, dfs(i))

    with open("moocast.out", "w") as output_file:
        output_file.write(str(numCanHear))




