# #Method 1: Using list
hash_list = [0]*11
n = [1,2,3,4,5,2,4,3,10,3,7,8,4,8,9]
m = [3,4,532,5,624,4525,66,7,43,32,5435,6,34]
for i in n:
    hash_list[i] += 1

for i in m:
    if i<1 or i>10:
        print(0)
    else :
        print(hash_list[i])

#Method 2: Using Dictionary
freq_map = dict()
for i in n:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1
print(freq_map)

for i in m:
    if i in freq_map:
        print(1)
    else:
        print(0)
        
