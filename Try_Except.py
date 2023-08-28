try:
    # value = 10/0
    numbers = int(input("enter numbers: ")) 
    print(numbers)
except ZeroDivisionError as err:
    print("Divided by zero")
except ValueError:
    print("invalid input")