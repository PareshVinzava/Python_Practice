#more about lists
"""
list is silimar to arry of other languages but more flexible
orderd
mutable
dynamic
nested
"""


a = [1,2,4,5,6,7,8]
a.append(["a","b","c","d"]) # append willl add whole list
print(a)

b = [1,2,4,5,6,7,8]
b.extend(["a","b","c","d"]) #extend will only add elemets 
print(b)

b.remove(6)
print(b)

b.pop()  # the plain pop will delete last element 
print(b)

b.pop(2) #if i want to remove perticular element in list using pop() then i have to write that elements index number in pop(index number) <-- this way
print(b)



