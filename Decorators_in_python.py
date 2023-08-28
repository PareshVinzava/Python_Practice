"""
Decorator is used for
- logging
- authentication
- instrumentation & timing functions
- rate-limiting 
- caching and more 
"""

# we can change the name of the function
def success(x):
    return print(x+1)

# here i have given second name to sam efunction 
successor = success

# so now i can use that new name for calling same function
successor(10)

# we can even delete name also

del success

successor(20)
# success(20)  #now i will not be able to use this name coz i have deleted this one

