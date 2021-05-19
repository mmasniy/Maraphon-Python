def bubble_sort(list_int):
    for i in range(len(list_int) - 1):
        for j in range(len(list_int) - 1 - i):
            if list_int[j] > list_int[j + 1]:
                list_int[j], list_int[j + 1] = list_int[j + 1], list_int[j]

    return list_int
