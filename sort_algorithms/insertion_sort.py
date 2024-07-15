def inserttion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i -1
        while temp < ls[j] and j > -1:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+ 1] = temp
    return print(ls)

ls = [2, 1, 3, 8, 7]


inserttion_sort(ls)