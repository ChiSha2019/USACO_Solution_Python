input_list = [1,2,3,4,5,5,6,7,8,8,8,9]
my_set = set()
result_list = []
'''
1. add input_list' element to a set one by one
2. While doing the adding, we check whether the element is already in the set beforehand
    2.1 if true put this element into the result list
    2.2 if false we store this element into set and keep looping the list
'''
for element in input_list:
    if element in my_set:
        result_list.append(element)
    else:
        my_set.add(element)

print(set(result_list))






