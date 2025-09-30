#Method 1: Using Loop
s = "racecar"
left = 0
right = len(s)-1
def checkPalindrome(s,left,right):
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
print(checkPalindrome(s,left,right))

#Method 2: Using Recursion
i = 0
j = len(s)-1
def checkPalindromeRecursion(s,i,j):
    if i >= j:
        return True
    if s[i] == s[j]:
        return checkPalindromeRecursion(s,i+1,j-1)
    else:
        return False
print(checkPalindromeRecursion(s,i,j))