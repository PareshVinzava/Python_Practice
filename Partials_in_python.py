# Partials functions allow us to fix a certain number of arguments of a function and generator a new function functools partial

# in simple word if i have function but i want so many variation of that  functon than
# intead of defining so many functions i can use partial function

#i have to import partial function from the functool


from functools import partial
from tokenize import Exponent # it is important to use partial function

# it is our normal function
def power(base,exponent):
    print(f"{base} to the power {exponent}")
    return print(base**exponent)

# now i want variations in function so ican use partial function

square = partial(power,exponent=2)
cube = partial(power,exponent=3)

#now check our variations and we can use our variation functions

square(4)
cube(2)


