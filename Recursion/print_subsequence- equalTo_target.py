#print the lost of all the subsequence that is equal to target
# This is also an example of backtracking
def print_subsequence(nums, target):
    result = []
    def backtrack(index, total, subset):
        if total == target:
            result.append(subset.copy())  
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        subset.append(nums[index])
        sum = total + nums[index]
        backtrack(index + 1, sum, subset)
        e = subset.pop()
        sum = sum - e
        backtrack(index + 1, sum, subset)
    backtrack(0, 0, [])
    return result

if __name__ == "__main__":
    nums = [5, 9, 4, 3, 1]
    print(print_subsequence(nums, 9))