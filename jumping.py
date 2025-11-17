import math

def jump_search(sorted_list, key):
    n = len(sorted_list)
    step = int(math.sqrt(n))
    prev = 0

    # Jump in steps until we find a block where the element may exist
    while prev < n and sorted_list[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    while prev < min(step, n) and sorted_list[prev] < key:
        prev += 1
        if prev == min(step, n):
            return -1

    # Check if found
    if prev < n and sorted_list[prev] == key:
        return prev

    return -1


# Test data
user_database = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
search_key_1 = "j"

# Test: find a user that exists
index_1 = jump_search(user_database, search_key_1)
if index_1 != -1:
    print(f"found '{search_key_1}' at index: {index_1}")
else:
    print(f"'{search_key_1}' was not found")
