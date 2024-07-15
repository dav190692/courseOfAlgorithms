def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list):
    mid_index =int(len(my_list) /2)

    if len(my_list) == 1:
        return my_list

    left = merge_sort(my_list[:mid_index])
    rigth = merge_sort(my_list[mid_index : ])

    return merge(left, rigth)





print(merge_sort([23, 12, 3, 45, 5, 67, 5, 67, 666, 234, 111, 1, 89, 98]))