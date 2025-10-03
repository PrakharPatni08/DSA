nums = [53,53,4321,6,432,65,23]
n = len(nums)
def bubbleSort(nums):
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
print(bubbleSort(nums))