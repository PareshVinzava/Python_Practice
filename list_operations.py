a = [1,2,3,4]
b = [1,2,3,4]

print(a is b) # is will return bool and checks both are same or not

a = [1,2,3,4,5,"a","b","d","e"]

a = [1,2,3,4,[1,2,3],"abc","def","ghi"]
print(a[1])
print(a[4])

print(a[0:5:2])
print(a[-1]) 
print(a[::-1])

print(a + ["jkl","mno"]) #concatenation of list

b = ["mango","kiwi","banana"]
b[0] ="apple" # it will replace mango with apple
print(b)

b[1:3] = ["no fruits"]
print(b)

b[1] = ["cherry","potato","dragon fruits"] #it will add a list at index place 1 and replaces no fruits
print(b)

#below syntax is important

c = [1,2,3,4,5,6,7,8]
c[0] = ["a","B","c","d"]  #this syntax for replacing element in list will add whole list in place 
print(c)

c = [1,2,3,4,5,6,7,8]
c[0:1] = ["a","B","c","d"]  #this syntax for replacing element in list will add only elements in list place 
print(c)
