with open("breedflip.in", "r") as input_file:
    gene_num = int(input_file.readline())
    gene_a = input_file.readline()
    gene_b = input_file.readline()
    num_consecutive_different_letter = 0
    num_flip = 0
    # check the start of a flipped block
    for i in range(0, gene_num):
        if gene_a[i] == gene_b[i]:
            num_consecutive_different_letter = 0
        else:
            if num_consecutive_different_letter == 0:
                num_flip += 1
            num_consecutive_different_letter += 1
    with open("breedflip.out", "w") as output_file:
        output_file.write(str(num_flip))


