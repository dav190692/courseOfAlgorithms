def swap(my_list, index1, index2):
    length_list = len(my_list)
    if index1 > length_list or index2 > length_list:
        raise IndexError('Index out of List')
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot (my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, rigth):
    if left < rigth:
        pivot_index  = pivot(my_list, left, rigth)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index + 1, rigth )
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)
    

ls = [23, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10]


print(quick_sort(ls))


    

