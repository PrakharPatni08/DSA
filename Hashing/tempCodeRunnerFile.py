freq_map = dict()
for i in n:
    print(n[i],i)
    if n[i] in freq_map:
        freq_map[n[i]] += 1
    else:
        freq_map[n[i]] = 1
print(freq_map)