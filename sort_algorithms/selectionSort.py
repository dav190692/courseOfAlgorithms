def selection_sort(ls):
    for i in range (len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        if i != min_index:
            ls[i], ls[min_index] = ls[min_index], ls[i]
    return ls



print(selection_sort([2, 1, 5, 4, 78, 56]))



# սա շատ հասարակ և էֆեկտիվ սորտավորման ալգորիթմ է ոչ մեծ զանգվածների կամ որոշ չափով սորտավորված զանգվածների համար
#  O(n^2) kam O(n)