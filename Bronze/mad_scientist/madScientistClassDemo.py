'''
1.understand the question
2.Think abt strategy
3.Translate your strategy into code

STRATGY:
 have num_flip = 0
 iterate through string A and B and compare them,
 if there is any different substring block, increase num_flip by 1
 how to represent the start of a different substring
'''
with open("breedflip.in", "r") as input_file:
    breed_num = int(input_file.readline())
    breed_a = input_file.readline()
    breed_b = input_file.readline()

    #last_isSame = True
    num_flip = 0
    '''
    for i in range(0, breed_num):
        if breed_a[i] != breed_b[i] and last_isSame:
            num_flip += 1
        last_isSame = breed_a[i] == breed_b[i]
    '''
    if breed_a[0] != breed_b[0]:
        num_flip += 1

    for i in range(1, breed_num):
        if breed_a[i] != breed_b[i] and breed_a[i-1] == breed_b[i-1]:
            num_flip += 1


    with open("breedflip.out", "w") as output_file:
        output_file.write(str(num_flip))

