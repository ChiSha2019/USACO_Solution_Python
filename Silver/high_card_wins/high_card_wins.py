

with open("highcard.in", "r") as input_file:
    N = int(input_file.readline())
    bessie = []
    elsie = []
    for i in range(N):
        elsie.append(int(input_file.readline()))
    elsie.sort()
    j = 0
    for i in range(1, 2*N+1):
        if j <N and elsie[j] == i:
            j += 1
        else:
            bessie.append(i)

    #greedy compare bessie and elsie from small to big,
    # use smallest from bessie to compare with elsie
    score = 0
    bessie_index = 0
    elsie_index = 0

    while bessie_index < N and elsie_index < N:
        if bessie[bessie_index] > elsie[elsie_index]:
            score += 1
            bessie_index += 1
            elsie_index += 1
        else:
            bessie_index += 1

    with open("highcard.out", "w") as output_file:
        output_file.write(str(score))
