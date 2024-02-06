def selection_sort(array):
    start, end = 0, len(array)
    while start < len(array):
        min_element = min(array[start:])
        min_index = array.index(min_element)
        array[start], array[min_index] = array[min_index], array[start]
        start += 1
    print(array)

selection_sort([9,8,5,2])