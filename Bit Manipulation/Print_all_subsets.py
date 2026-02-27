def print_subsets(nums):
    n = len(nums)
    result = []
    total_subsets = 1<<n
    for num in range(0, total_subsets):
        lst = []
        for i in range(0, n):
            if num & (1<<i) != 0:
                lst.append(nums[i])
        result.append(lst)
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    print(print_subsets(nums))
        
