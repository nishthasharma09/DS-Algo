def minimumDifference(nums, k):
    if len(nums) == 1:
        return 0
    else:
        mini = nums[1] - nums[0]
        left, right = 0, 1
        while left < right and right < len(nums):
            curr_diff = nums[right] - nums[left]
            if right < len(nums):
                right += 1
            else:
                left += 1
            mini = min(mini, curr_diff)
        return mini
    
print(minimumDifference())