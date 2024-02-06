# def insertion_sort(customList):
#     for i in range(1, len(customList)):
#         key = customList[i]
#         j = i-1
#         while j >=0 and key < customList[j]:
#             customList[j+1] = customList[j]
#             j -= 1
#         customList[j+1] = key
#     print(customList)

def insertion_sort(array):
    sorted_index = 0
    while sorted_index < len(array):
        j = sorted_index-1
        key = array[sorted_index]
        while key < array[j] and j >= 0:
            array[j], array[j+1] = array[j+1], array[j]
            j-=1
        sorted_index += 1
    print(array)
    
 
insertion_sort([5,3,4,7,2,8,6,9,1]) 