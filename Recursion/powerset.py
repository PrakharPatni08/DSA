#Print all the subsets of a list
def print_subsets(nums):
    result = []
    
    def solve(index, subset):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        solve(index + 1, subset)
        subset.pop()
        solve(index + 1, subset)
    
    solve(0, [])
    return result

if __name__ == "__main__":
    nums = [5, 9, 7]
    print(print_subsets(nums))