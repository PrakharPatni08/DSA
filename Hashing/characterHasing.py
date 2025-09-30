s = "aaysysiabdjd"  # Make it a string directly
q = ["a","y","s","b","d","x","z"]
hash_list = [0]*27
n = len(s)

for ch in range(0, n):
    ascii_val = ord(s[ch])
    index = ascii_val - 97
    hash_list[index] += 1

print(hash_list)

for i in q:
    ascii_val = ord(i)
    index = ascii_val - 97
    print(hash_list[index])