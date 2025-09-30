result = []
def oneToN(i, N):
    if i > N:
        return result
    oneToN(i + 1, N)
    result.append(N - i + 1)  # This gives: 1, 2, 3, ..., 15
    return result

print(oneToN(1, 15))