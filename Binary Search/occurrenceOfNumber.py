nums = [1,1,1,2,3,3,4,5,5,5,5,6,7,9]
def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else :
            low = mid + 1
    return lb

def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ub = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else :
            low = mid + 1
    return ub

def countOccurrence(nums, target):
    lb = lowerBound(nums, target)
    up = upperBound(nums, target)
    count = up - lb
    return count

print(countOccurrence(nums, 8))