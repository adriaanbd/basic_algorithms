# Searching algorithms


def linear_search(array, val, len):
    answer = 'Not found'
    index = 0
    while index < len:
        if array[index] == val:
            answer = index
        index += 1
    return answer


def better_linear_search(array, val, len):
    answer = 'Not found'
    index = 0
    while index < len:
        if array[index] == val:
            return index
        index += 1
    return answer


def sentinel_linear_search(array, val, len):
    last = array[-1]
    array[-1] = val
    index = 0
    answer = 'Not found'
    while array[index] != val:
        index += 1
    array[-1] = last
    if index < len - 1 or array[-1] == val:
        return index
    return answer


def recursive_linear_search(array, val, len, i):
    while i < len:
        if array[i] == val:
            return i
        i += 1
        recursive_linear_search(array, val, len, i)
    return "Not found"


array = [11,9,3,7,4,8]
val = 8
n = len(array)

print(linear_search(array, val, n))
print(better_linear_search(array, val, n))
print(sentinel_linear_search(array, val, n))
print(recursive_linear_search(array, val, n, 0))
