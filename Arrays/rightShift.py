arr1 = [1,2,2,3,4,5,5,6,6,8,9,9,9]
n = len(arr1)
temp = arr1[n-1]
def rightShift(arr1):
    for i in range(n-2, -1, -1):
         arr1[i+1] = arr1[i]
    arr1[0] = temp
    return arr1
print(rightShift(arr1))


arr = [1,2,2,3,4,5,5,6,6,8,9,9,9]
m = len(arr)
tem = arr[n-1]
def rightShift1(arr):
    for i in range(0,m-2):
        arr[i+1] = arr[i]
    arr[0] = tem
    return arr
print(rightShift(arr))

nums = [1,2,2,3,4,5,5,6,6,8,9,9,9]
def kRightShift(nums, k):
    m1 = len(nums)
    for j in range(k): 
        tem1 = nums[m1-1] 
        for i in range(m1-2, -1, -1): 
            nums[i+1] = nums[i]
        nums[0] = tem1  
    return nums
print(kRightShift(nums,3))