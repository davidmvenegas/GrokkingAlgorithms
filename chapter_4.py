def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([4, 2, 3, 1]))
print(quicksort([10, 5, 2, 3, 1, 4, 6, 7, 8, 9]))
print(quicksort([10, 5, 2, 3, 1, 4, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
