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


def fib_generator(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1

"""
Closures
"""


"""Without closures causes an error because data doesnt exist anymore"""
def outer(par):
    loc = par


var = 1
outer(var)

print(var)
print(loc) 


"""With closures you can persist data in which the scope that it was created
doesnt exist anymore"""
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())


"""
Files
"""

