with open("highcard.in", "r") as input_file:
    N = int(input_file.readline())
    bessie = []
    elsie =[]
    for i in range(N):
        elsie.append(int(input_file.readline()))
    elsie.sort()

    j= 0
    for i in range(1,2*N+1):
        if j < N and elsie[j] == i:
            j += 1
        else:
            bessie.append(i)

    #greedy compare bessie and elsie from small to big
    #use the smallest from bessie that is just enough to win elsie

    score = 0
    b_index = 0
    e_index = 0

    while b_index <N and e_index < N:
        if bessie[b_index] > elsie[e_index]:
            score += 1
            b_index += 1
            e_index += 1
        else:
            b_index += 1

    with open("highcard.out", "w") as output_file:
        output_file.write(str(score))