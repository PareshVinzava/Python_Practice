# Simple Decorator 


def our_decorator(func):

    def function_wrapper(x):
        print("Before Calling " + func.__name__)
        func(x)
        print("After Calling " + func.__name__)

    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))


foo("hi")
foo = our_decorator(foo)
foo(42)