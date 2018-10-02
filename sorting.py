
def selection_smallest(array, len):
    index = 0
    smallest = array[index]
    while index < len:
        if array[index] < smallest:
            smallest = array[index]
        index += 1
    return smallest


def selection_sort(array, len):
    outer_i = 0
    while outer_i < len - 1:
        smallest = outer_i
        inner_i = outer_i + 1
        while inner_i < len:
            if array[inner_i] < array[smallest]:
                smallest = inner_i
            inner_i += 1
        # save elements to swap
        a = array[outer_i]
        b = array[smallest]
        # swap elements
        array[outer_i] = b
        array[smallest] = a
        outer_i += 1  # next outer index
    return array

array = [12,9,3,7,14,11]
n = len(array)
print(selection_smallest(array, n))
print(selection_sort(array, n))

