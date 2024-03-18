def merge(nums1, m, nums2, n):
    left, right = 0, n
    left_for_nums2 = 0
    while left_for_nums2 < n:
        print(f"nums1 = {nums1[left]} nums2 = {nums2[left_for_nums2]}")
        if nums1[left] > nums2[left_for_nums2]:
            nums1.insert(left, nums2[left_for_nums2])
            nums1.pop(-1)
        else:
            nums1.insert(left+1, nums2[left_for_nums2])
            nums1.pop(-1)
        left += 2
        left_for_nums2 += 1
    print(nums1)
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))