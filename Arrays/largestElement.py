nums = [213,432,23,43,31,21432,1542]
n = len(nums)
max_index = 0
def largestElement(nums):
    for i in range(0,n,1):
        if nums[i] > nums[max_index]:
            nums[i], nums[max_index] =  nums[max_index],nums[i]
    return nums[max_index]


def secondLargest(nums):
    first = float("-inf")
    second = float("-inf")
    for i in range(0,n):
        first = max(first, nums[i])
    for i in range(0,n):
        if nums[i] != first and nums[i] > second:
            second = nums[i]
    return second

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
def sorted(arr):
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
print(sorted(arr))
