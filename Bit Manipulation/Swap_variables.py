#Swappping Two Variable without using Third variable
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

if __name__ == "__main__":
    print(swap(32, 23))