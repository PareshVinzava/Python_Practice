#while loop is used for indefined iterations




n = 0

while n <= 5:
    print("value of n is = ",n)
    n += 1 



c = 0
a = [1,2,3,4,5]
while a:
    c += 1
    print("This iteration number :",c)
    print(a)
    a.pop()
      

# while loop within while loop

a = [1,2,3,4,5]
while a:
    print(">",a.pop(0))
    b = ["first","second"]
    while b:
        print(">>>",b.pop(0))



# break statement 

n = 0

while n <= 5:
    print("value of n is = ",n)
    n += 1
    if n == 2:
        break

# Continue Statement

while n <= 5:
    print("value of n is = ",n)
    n += 1
    if n == 2:
        continue
    print("hello")


