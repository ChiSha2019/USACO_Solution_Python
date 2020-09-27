#use for loop to read from input_in_class_exercise.in
#print out those who adds up to 20
#output in your terminal should be like:
#6 9 5
#3 4 13
#11 0 9


#to solve, you need to split, then map from string to int
f = open('input_in_class_exercise.in', 'r')
for each_line in f:
    line_list = each_line.split()
    sum = 0
    for element in line_list:
        sum += int(element)

    if sum == 20:
        print(each_line)
    #line_list_int = map(int, line_list)
    #if sum(line_list_int) == 20:
     #   print(each_line)
f.close()