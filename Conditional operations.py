#Conditional operations


if 50>30:
    print("50 is indeed a larger than 30")

age = 20

if age > 18:
    print("this person is an adult")


x = [50,"cat","apple"] 

if 60 in x:
    print("60 is in list x")
elif "cat" in x:
    print("cat is list x")
else:
    print("this will not be printed")


#  new thing learned 
#Conditional Expression (Python's Ternary Operation)

age =  28

x = "adult" if age > 20 else "child"
print(x)

#pass Statement

if age > 16:
    pass







