nums = [3,321,412,431,431,5421,4,21,44]
n = len(nums)
def insertionSort(nums):
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
print(insertionSort(nums))