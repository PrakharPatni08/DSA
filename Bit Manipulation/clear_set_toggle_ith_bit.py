#Clear the ith Bit
def clear(N,i):
    return N & (~(1<<i))

# Set The ith Bit
def set(N,i):
    return N | (1<<i)

# Toggle the ith Bit
def toggle(N,i):
    return N ^ (1<<i)

if __name__ == "__main__":
    print(clear(13,2))
    print(set(9,2))
    print(toggle(9,1))