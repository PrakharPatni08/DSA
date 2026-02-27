# Return The elemet that hhas the frequency of one

#Brute Force
def single_element(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else :
            hash_map[arr[i]] = 1
    a = []
    for key, value in hash_map.items():
        if value == 1:
            a.append(key) 
    return a


#Optimal Trick using XOR but only works when there is only a single element that is unique not for multiple single elemets
def XOR_Trick(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans

if __name__ == "__main__":
    arr = [1,7,5,7,1,9,9]
    print(single_element(arr))
    print(XOR_Trick(arr))
