def validPalindrome(s):
    left, right = 0, len(s) - 1
    skipFlag = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if skipFlag == False:
                skipFlag = True
                if s[left+1:right+1] == s[left+1:right+1][::-1]:
                    left+=1
                else:
                    right -=1 

            else:
                return False
    return True

print(validPalindrome("cbbcc"))