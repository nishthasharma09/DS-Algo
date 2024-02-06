# MY ALGORITHM

def bubble_sort(array):
    index = 1
    while index < len(array):
        for i in range(len(array) - index):
            #print(range(len(array) - index))
            if array[i+1] < array[i]:
                array[i], array[i+1] = array[i+1], array[i]
        print(array)
        index += 1

array = [10,9,8,7,6]
bubble_sort(array)

# GIVEN ALGORITHM IN COURSE

def bubble_sort_udemy(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
  
bubble_sort_udemy(array)
