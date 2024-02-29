def largest_subarray_of_sum_k(array, k):
    left, right = 0, 0
    window_sum = 0
    max_size = 0
    while right < len(array):
        window_sum += array[right]
        while window_sum > k and left <= right:
            window_sum -= array[left]
            left += 1
        if window_sum == k:
            max_size = max(max_size, (right - left) + 1)
            window_sum -= array[left]  # Adjust window sum to consider the next subarray
            left += 1
        right += 1
    print(max_size)
            
largest_subarray_of_sum_k([2,3,2,5,1,1,1,1,1], 5)