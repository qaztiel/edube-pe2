"""
fib(n)

fib(1) = 1
fib(2) = 1

fib(3) = 2

"""

def fib(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(3))

