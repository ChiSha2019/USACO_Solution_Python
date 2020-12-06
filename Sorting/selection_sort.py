def selection_sort(list_to_sort):
    #Index of the first element of the right part
    for i in range(len(list_to_sort)):
        #find min element in the right unsorted array
        min_idx = i

        for j in range(i + 1, len(list_to_sort)):
            '''
            will be excuted n-i times
            '''
            if list_to_sort[min_idx] > list_to_sort[j]:
                min_idx = j

        #swap between the min element in right part with the first elemnt
        #of right part
        '''
        temp = list_to_sort[min_idx]
        list_to_sort[min_idx] = list_to_sort[first_element_of_right_index]
        list_to_sort[first_element_of_right_index] = temp
        '''
        list_to_sort[min_idx],list_to_sort[i] = list_to_sort[i], list_to_sort[min_idx]

    return list_to_sort


list_to_sort = [5, 1, 12, -5, 16, 2, 12, 14]
sorted_list = selection_sort(list_to_sort)
print(sorted_list)