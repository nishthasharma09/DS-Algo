def max_from_window(array: list, k: int):
    max_sum = 0
    for i in range(0, len(array) -k +1):
        sub = array[i:i+k]
        sumi = 0
        for j in sub:
            sumi += j
        print(sub, sumi)
        if sumi > max_sum:
            max_sum = sumi
    print(max_sum)

max_from_window([3,2,4,5,1,1,1,1,2,3,3], 5)