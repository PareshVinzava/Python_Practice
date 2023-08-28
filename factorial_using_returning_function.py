
def factorial(n):
    if type(n) == int and n >= 0:

        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    else:
        raise TypeError ("n has to a positive intizer or zero")

print(factorial(4))

print(factorial(-4)) # here my error will going to be raised  
