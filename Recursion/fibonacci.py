# Fibonacci series using iteration
def fibonacci(n):
    a = 0
    b = 1
    if n == 1 or n == 0:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")
    return
print(fibonacci(10))

# Fibonacci series using recursion
def fibonacciRecursion(n):
    if n == 0 or n == 1:
        return n
    return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)
print(fibonacciRecursion(11))