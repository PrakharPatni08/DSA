def oneToN(i,N):
    if i>N:
        return
    print(i)
    oneToN(i+1,N)
print(oneToN(12,15))