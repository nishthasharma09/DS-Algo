import math

def selection_sort(array):
    start, end = 0, len(array)
    while start < end:
        minimum = start
        for i in range(start, end):
            if array[i] < array[minimum]:
                minimum = i
        array[start], array[minimum] = array[minimum], array[start]
        start+=1
    return array

def bucket_sort(customList):
    # calculate no of buckets & make empty array
    no_of_buckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    array = []
    for i in range(no_of_buckets):
        array.append([])
    
    # insert elements into designated bucket [[1,2,3], [4,5,6], [7,8,9]]
    for j in customList:
        index_b = math.ceil(j*no_of_buckets/maxValue)
        array[index_b-1].append(j)
    
    # sort each bucket 
    for i in range(no_of_buckets):
        array[i] = selection_sort(array[i])

    # merge the buckets
    k = 0
    for i in range(no_of_buckets):
        for j in range(len(array[i])):
            customList[k] = array[i][j]
            k+=1
    print(customList)

bucket_sort([1,2,4,91,93,95])  



selection_sort([9,2,6,3,12,5])