#Using Left Shift
def check_using_left_shift(N,i):
    if (N&(1<<i)) != 0:
        return True
    else:
        return False
    
#Using Right Shift Operator
def check_using_right_shift(N,i):
    if ((N>>i) & 1) != 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(check_using_left_shift(13,1))
    print(check_using_right_shift(13,0))