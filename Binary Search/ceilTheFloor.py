nums = [3,4,4,4,8,9,9,10,12,12,14,15]
def ceilTheFloor(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1
    if target > nums[high]:
        floor = nums[high]
    if target < nums[low]:
        ceil = nums[low]
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            ceil = nums[mid]
            floor = nums[mid]
        elif nums[mid] > target:
            high = mid - 1
            ceil = nums[mid]
        else:
            low = mid + 1
            floor = nums[mid]
    return [floor, ceil]
out = ceilTheFloor(nums, 11)
print(out)
