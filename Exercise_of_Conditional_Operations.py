# Determine if user input is odd or even


user_input = int(input("Please enter number between 1 to 20:  "))

if user_input >= 1 and user_input <= 20:
    print(" you have entered a valid number : ")

    if user_input % 2 == 0:
        print("your number is even")
    elif user_input % 2 == 1:
        print("your number is odd")
else:
    print("your input is invalid ")
 