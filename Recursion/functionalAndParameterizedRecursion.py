#Parametized Recursion
def func(sum,i,n):
    if i>n:
        return sum
    return func(sum+i,i+1,n)
print(func(0,1,5))

#Functional Recursion
def Sum(n):
    if n == 1:
        return 1
    return n+Sum(n-1)
print(Sum(6))