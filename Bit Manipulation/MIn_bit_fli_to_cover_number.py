#code for finding the minimum no. of bit flips to convert a number to a required number(start, goal)
def min_bit_flip(start, goal):
    n = start ^ goal
    b = bin(n).count("1")
    return b

if __name__ == "__main__":
    print(min_bit_flip(10,7))