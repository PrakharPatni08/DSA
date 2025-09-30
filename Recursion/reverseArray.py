nums = [5,4,3,2,1,0]
left = 0
n = len(nums)
right = n
def reverse(nums,left,right):
    if left >= right:
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    return reverse(nums,left+1,right-1)
print(reverse(nums,0,5))