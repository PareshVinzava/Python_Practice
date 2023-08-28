# iterating through iterator 

# iter(name of iterable)
# next(name of variable in which iter is saved)

my_list = [1,3,2,4,5,6,7,8]

a = iter(my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

my_list2 = [1,3,2,4,5,6,7,8]
c = iter(my_list2)

while True:
    try:
        p = next(c)
        print(p)
    except StopIteration:  #when this exception is raised break while loop
        break