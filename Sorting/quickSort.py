nums = [9,8,7,4,5,6,2,1,3]
low = 0
high = len(nums)-1
def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i] <= pivot and i <= high-1:
            i += 1
        while nums[j] > pivot and j >= low+1:
            j -= 1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quickSort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quickSort(nums, low, p_index-1)
        quickSort(nums, p_index+1, high)
    return nums
print(quickSort(nums,low,high))