def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i -1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j-=1
        list[j+1] = key
    return list

arr = [4,3,2,10,12,1,5,6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
