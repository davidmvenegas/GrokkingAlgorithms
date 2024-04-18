cache = {}


def in_cache(num):  # O(1)
    if num in cache:  # return a hit if the number is in the cache
        return True
    else:  # otherwise, add it and return false
        cache[num] = True
        return False


print(in_cache(5))
print(in_cache(5))
print(in_cache(5))
print(in_cache(6))
print(in_cache(6))
