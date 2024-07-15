def bubble_sort (my_list):
    for i in range(len(my_list) -1, 0, -1):
        swapped = False
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list [j + 1], my_list [j]
                swapped = True
        if not swapped:
            break

    return print(my_list)



bubble_sort([1, 3, 6, 7, 2, 45, 9])