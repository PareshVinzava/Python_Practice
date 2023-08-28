#return fibonacci series of numbers given by user 
us_in = int(input("enter a number :  "))

i = 1
out = [1,1]

if us_in == 0:
    print("[ ]")
elif us_in == 1:
    print("[1]")
elif us_in == 2:    
    print("[1,1]")
elif us_in > 2: 
    while i<(us_in-1):
        b = out[i] + out[i-1]
        out.append(b)
        i += 1
    print(f"Your fibonacci series is {out}") 









