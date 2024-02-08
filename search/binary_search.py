array = [1,2,3,4,5,6,7,8,9]

def binary_search(array, element):
    start, end = 0, len(array) - 1
    middle = (start+end)//2
    print(start, middle, end)
    while not(array[middle] == element):
        if element < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start+end)//2
        print(start, middle, end)
    return array[middle]

def binary_search_recursive(array, element):
    if len(array) == 1:
        if array[0] == element:
            return array[0]
        else:
            return None
    else:
        middle = len(array) // 2
        if array[middle] == element:
            print(f"Element {array[middle]} found at {middle}")
        elif array[middle] > element:
            binary_search_recursive(array[0: middle],element)
        else:
            binary_search_recursive(array[middle:], element)

def binary_search_recursive_new(array, start, end, element):
    middle = (start + end) // 2
    if array[middle] == element:
        print(f"Element found at {middle}")
        return
    else:
        if array[middle] > element:
            binary_search_recursive_new(array, start, middle,element)
        else:
            binary_search_recursive_new(array, middle, end, element)

binary_search_recursive_new(array,0, len(array), 6)

