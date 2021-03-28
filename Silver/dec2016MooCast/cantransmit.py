with open("1.in", "r") as input_file:
    N = int(input_file.readline())
    x = []
    y = []
    r = []
    for i in range(N):
        listcow = input_file.readline().split()
        x.append(int(listcow[0]))
        y.append(int(listcow[1]))
        r.append(int(listcow[2]))

canTransmit = [[False] * N for _ in range(7)]  # n by n array

for i in range(N):
    for j in range(N):
        print("i=" + str(i))
        print("j=" + str(j))
        square_dist = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
        print("squared dis=" + str(square_dist))
        print("radius square is=" + str(r[i] * r[i]))
        print(square_dist <= r[i] * r[i])
        canTransmit[i][j] = (square_dist <= r[i] * r[i])
        print(canTransmit)


