#find second mostly occured element?
input_list = [1,2,3,4,5,5,6,7,8,8,8,9]
input_list = [1,2,3,4,5,6,7,8]
'''
1.create a dictionary, with key as elements, value as frequency
    1.1 iterate through input_list, check if element is already in the dictionary
        if true: increase frequency by 1
        else: add this key into dictionary, with frequency 1
2.return the key with greatest value
'''
my_dict = {}
max_freq = -1
second_max_freq = -2
key_of_second_max_freq = -999
#O(n)
for element in input_list:
    if element in my_dict:
        my_dict[element] += 1
        if my_dict[element] >= max_freq:
            second_max_freq = max_freq
            max_freq = my_dict[element]
            key_of_second_max_freq = element

    else:
        my_dict[element] = 1

print(key_of_second_max_freq)

