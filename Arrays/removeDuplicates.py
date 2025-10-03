nums = [1,2,2,3,4,5,5,6,6,8,9,9,9]
n = len(nums)
freq_map = dict()
def uniqueElements(nums):
    for i in range(0, n):
        freq_map[nums[i]] = 0
    
    j = 0
    for k in freq_map:
        nums[j] = k
        j += 1
    
    return nums[0:j]
print(uniqueElements(nums))

arr = [1,2,2,3,4,5,5,6,6,8,9,9,9]
def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return arr
    i = 0
    j = 1
    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
        j += 1
    return arr[0:i+1]
print(removeDuplicates(arr))

