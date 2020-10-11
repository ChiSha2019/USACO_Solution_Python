with open("breedflip.in", "r") as input_file:
    gene_num = int(input_file.readline())
    gene_a = input_file.readline()
    gene_b = input_file.readline()
    num_flip = 0
    wereLastCharsSame = True
    for i in range(0, gene_num):
        #check the start of a flipped block
        if gene_a[i] != gene_b[i] and wereLastCharsSame:
            num_flip += 1
        wereLastCharsSame = gene_a[i] == gene_b[i]

    with open("breedflip.out", "w") as output_file:
        output_file.write(str(num_flip))
