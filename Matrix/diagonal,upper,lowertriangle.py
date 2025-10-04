nums = [[1,2,3],[4,5,6],[7,8,9]]
def uppperTriangle(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if j >= i:
                print(nums[i][j], end = " ")
            else :
                print("*", end = " ")
        print()

def lowerTriangle(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if j <= i:
                print(nums[i][j], end = " ")
            else :
                print("*", end = " ")
        print()

def diagonal(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if j == i:
                print(nums[i][j], end = " ")
            else :
                print("*", end = " ")
        print()

print(uppperTriangle(nums))
print(lowerTriangle(nums))
print(diagonal(nums))