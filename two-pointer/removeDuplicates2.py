def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, 1
    while right < len(nums) and left < right:
        if nums[right] == nums[left]:
            if ((right - left) + 1) > 2:
                nums.pop(left)
            else:
                right += 1
        else:
            left = right
            right = left + 1
    return len(nums)

print(removeDuplicates([1,1,1,2,2,3]))