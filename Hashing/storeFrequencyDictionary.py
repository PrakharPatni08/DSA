#Method 1: Using if-else
freq_map = dict()
nums = [1,2,3,4,2,34,5,3,2,4,2,4,2,4,5,7]
n = len(nums)
for i in range(0,n):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)

#Method 2: Using hash_map.get() function
hash_map = {}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)