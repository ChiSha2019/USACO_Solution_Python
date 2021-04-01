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
    canTransmit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            square_dist = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            canTransmit[i][j] = (square_dist <= r[i] * r[i])