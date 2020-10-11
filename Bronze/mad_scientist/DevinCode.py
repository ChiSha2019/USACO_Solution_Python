with open("breedflip.in", "r") as input_file:
    breed_num = int(input_file.readline())
    breed_a = input_file.readline()
    breed_b = input_file.readline()

    num_flip = 0
    i = 0
    while i< breed_num:
        if breed_a[i] != breed_b[i]:
            num_flip += 1
            while breed_a[i] != breed_b[i]:
                i +=1
        i += 1
    with open("breedflip.out", "w") as output_file:
        output_file.write(str(num_flip))
