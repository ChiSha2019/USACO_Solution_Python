with open("buckets.in", "r") as input_file:
    for i in range(10):
        s = input_file.readline()
        for j in range(10):
            if s[j] == 'B':
                barn_i = i
                barn_j = j
            if s[j] == 'R':
                rock_i = i
                rock_j = j
            if s[j] == 'L':
                lake_i = i
                lake_j = j
    dist_br = abs(barn_i - rock_i) + abs(barn_j - rock_j)
    dist_bl = abs(barn_i - lake_i) + abs(barn_j - lake_j)
    dist_rl = abs(rock_i - lake_i) + abs(rock_j - lake_j)

    #b,l,r at same line and r in between b,l
    if (barn_i == lake_i or barn_j == lake_j) and dist_bl == dist_br + dist_rl:
        ans = dist_bl + 1
    else:
        ans = dist_bl - 1

with open("buckets.out", "w") as output_file:
    output_file.write(str(ans))
    output_file.write("\n")