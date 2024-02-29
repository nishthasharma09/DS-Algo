def max_from_window(array: list, k: int):
    max_sum = 0
    left, right = -1 , 0
    while right < len(array):
        if right - left != k:
            right += 1
        else:
            left+=1
            right+=1
            sumi = sum(array[left:right])
            print(array[left:right])
            if sumi > max_sum:
                max_sum = sumi
    print(max_sum)

def max_sum_subarray(arr, k):
    if k > len(arr):
        return "Window size is greater than array length"
    
    max_sum = sum(arr[:k])  # Calculate sum of the first window
    window_sum = max_sum
    
    # Iterate through the array, sliding the window and updating the maximum sum
    for i in range(1, len(arr) - k + 1):
        print(i, arr[i])
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]  # Update window sum
        max_sum = max(max_sum, window_sum)  # Update max_sum if needed
    
    return max_sum

max_sum_subarray([3,2,4,5,1,1,1,1,2,3,3], 5)