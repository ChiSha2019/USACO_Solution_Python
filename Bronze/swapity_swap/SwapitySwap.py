def reverse(array, start: int, end: int) -> list:
    i = start - 1
    j = end - 1
    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    return array


with open("swap.in", 'r') as input_file:
    input_line1 = input_file.readline().split()
    input_line2 = input_file.readline().split()
    input_line3 = input_file.readline().split()
    n = int(input_line1[0])
    k = int(input_line1[1])
    a1 = int(input_line2[0])
    a2 = int(input_line2[1])
    b1 = int(input_line3[0])
    b2 = int(input_line3[1])
    isCyclic = False
    cows = []
    cows_copy = []
    for i in range(0, n):
        cows.append(i + 1)
        cows_copy.append(i + 1)

    ''' dont use
    cows: list = list(range(1, n + 1))
    cows_copy = cows[:]
    '''

    for i in range(0, k):
        cows = reverse(cows, a1, a2)
        cows = reverse(cows, b1, b2)
        if cows == cows_copy:
            period = i + 1
            isCyclic = True
            break

    if isCyclic:
        num_iteration = k % period
        # redundant computation
        for i in range(0, num_iteration):
            cows = reverse(cows, a1, a2)
            cows = reverse(cows, b1, b2)

    with open("swap.out", "w") as output_file:
        for item in cows:
            output_file.write(str(item) + "\n")
