# Fibonacci


def fib(n):
    
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    res = fib(n - 1) + fib(n - 2)
    return res

x = int(input('Enter the number you would like to know in the sequence: '))
print(fib(x))
        