import random


def quicksort(array):
    # if the length of the array is less than 2, return the array
    if len(array) < 2:
        return array
    else:
        # create a pivot point
        pivot = random.choice(array)
        less = [i for i in array[1:] if i <= pivot]  # gather all numbers <= the pivot
        greater = [i for i in array[1:] if i > pivot]  # gather all numbers > the pivot

        # return the less array, pivot, then greater array (...so it's sorted!)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([4, 2, 3, 1]))
print(quicksort([10, 5, 2, 3, 1, 4, 6, 7, 8, 9]))
print(quicksort([10, 5, 2, 3, 1, 4, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
