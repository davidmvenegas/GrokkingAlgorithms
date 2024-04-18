def find_smallest_idx(arr):
    # store the smallest value and index
    smallest, smallest_idx = arr[0], 0

    # go through the array from left to right, updating the smallest
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    # return your spoils
    return smallest_idx


def selection_sort(arr):
    new_arr = []

    # for every number, add the smallest to the new array
    for _ in range(len(arr)):
        smallest_idx = find_smallest_idx(arr)
        smallest = arr.pop(smallest_idx)
        new_arr.append(smallest)

    # you've won, stop gloating
    return new_arr


my_list = [5, 3, 6, 2, 10]
print(selection_sort(my_list))  # => [2, 3, 5, 6, 10]
