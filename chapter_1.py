def binary_search(list, answer):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(list) - 1

    # while you haven't narrowed it down to one element...
    while low <= high:
        # ...check the middle element
        mid = (low + high) // 2
        guess = list[mid]

        # CASE 1: found the answer
        if guess == answer:
            return mid
        # CASE 2: too low
        if guess < answer:
            low = mid + 1
        # CASE 3: too high
        if guess > answer:
            high = mid - 1

    return None


my_list = [1, 3, 5, 7, 9]
#          0  1  2  3  4

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
print(binary_search(my_list, 9))  # => 4
