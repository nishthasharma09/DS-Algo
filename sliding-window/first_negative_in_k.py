def lengthOfLongestSubstring(s: str) -> int:
    left, right = 0, 1
    # # if len(s) == 0:
    # maxLength = 0
    # # else:
    # #     maxLength = 1
    while right < len(s):
        print(f"{s[right]} in {s[left:right]}")
        if s[right] in s[left:right]:
            left += 1
        else:
            right += 1
        maxLength = max(maxLength, right - left)
    print(maxLength)

lengthOfLongestSubstring("")