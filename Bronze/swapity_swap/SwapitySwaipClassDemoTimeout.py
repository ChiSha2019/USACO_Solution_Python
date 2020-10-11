def reverse(array, start: int, end: int) -> list:
    i = start - 1
    j = end -1
    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    return array


with open("swap.in", "r") as input_file:
    line1 = input_file.readline().split()
    line2 = input_file.readline().split()
    line3 = input_file.readline().split()
    n = int(line1[0])
    k = int(line1[1])
    a1 = int(line2[0])
    a2 = int(line2[1])
    b1 = int(line3[0])
    b2 = int(line3[1])

    cows = []
    for i in range(0, n):
        cows.append(i+1)

    for i in range(0,k):
        cows = reverse(cows,a1, a2)
        cows = reverse(cows,b1, b2)
        with open("swap.out", "w") as output_file:
            for item in cows:
                output_file.write(str(item) + "\n")

