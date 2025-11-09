def bubble_sort(to_sort):
    for i in range(len(to_sort) - 1):
        for j in range(len(to_sort) - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort

