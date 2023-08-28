# Dictionary
"""
keys should be always immutable(int,str..) and unique
if i give same key again and again it will be over write last key value pair

"""

#defining dict.
# 1st way to define dictionary
d = { "banana":"yellow","orange":"orange","tomato":"red"}
print(d)


# 2st way to define dictionary
d = dict([("banana","yellow"),("orange","orange"),("tomato","red")])
print(d)


#same keys will overwrite older keys 
d = {"banana":"yellow","banana":"pink"}
print(d)

# VALUES  can be duplicated 
d = {"apple":"yellow","banana":"yellow","tomato":"red","bord":"black"}
print(d) 

#how to get value of key
c = d["apple"]
print(c)

#change value of any key
d["apple"] = "red"
print(d)

#remove key value pair
del d["apple"]  #here i have to write key name 
print(d)

# get method 

q = d.get("tomato")
print(q)
                     #benifit of using get method is that if that key is not in dictionary it will not givr error or won't stop our code but instead it will return none
r = d.get("violate")
print(r)

# items method 
s = d.items()  # item method will give to tuple of key value pair
print(s)

#keys() method 
t = d.keys() # it will retuns tuple containings all the keys 
print(t)

#values() method 
u = d.values() # it will gives tuple containing all the values
print(u)

#popitem() method 

v= d.popitem() #popitem method returns last entered key value pair
print(v)

# update() method is used for merging two dictionaries

dict1 = {1:1,2:2,3:3,4:4}
dict2 = {5:5,6:6,7:7,8:8}

dict1.update(dict2)   # so this way by using update method we can merge two dictionaries 

print(dict1)