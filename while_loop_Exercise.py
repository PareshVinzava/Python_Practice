


user_input = int(input(" Enter number: "))
number = user_input

fac = 1

if number == 0:
    result = 1
else:
    while number >= 1:
        fac = fac*number
        number = number -1 
        result = fac
print(f"Factorial of {user_input} is {result}")