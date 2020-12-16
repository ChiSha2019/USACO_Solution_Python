
'''
/*
 * Strategy:
 * 1.read in the line as a 2D array
 * 2.reversely map the 2D array value to index
 * 3.compare vertically the 2D array to check consistency
 * */
'''
with open("1.in", "r") as input_file:
    line1 = input_file.readline().split()
    K = int(line1[0])
    N = int(line1[1])
    list_of_list = []
    for i in range(0, K):
        inner_list1 = input_file.readline().split()
        '''minus 1 because I want to use i directly as index'''
        inner_list = [int(i)-1 for i in inner_list1]
        list_of_list.append(inner_list)

    reverseMap = [[-1 for _ in range(N)] for __ in range(K)]
    for i in range(0, K):
        for j in range(0, N):
            reverseMap[i][list_of_list[i][j]] = j

    print(reverseMap)
    count = 0

    for left in range(0, N-1):
        for right in range(left + 1, N):
            is_greater = reverseMap[0][right] > reverseMap[0][left]
            isThisColumnConsistent = True
            for row in range(1, K):
                print(reverseMap[row][left])
                print(reverseMap[row][right])
                if (reverseMap[row][right] > reverseMap[row][left]) != is_greater:
                    print("exe")
                    isThisColumnConsistent = False
                    break
            print("isThisColumnConsistent "
                  ""
                  "= " + str(isThisColumnConsistent))
            if isThisColumnConsistent:
                print(str(left +1) + " " + str(right+1))
                count += 1

    with open("gymnastics.out", "w") as output_file:
        output_file.write(str(count))