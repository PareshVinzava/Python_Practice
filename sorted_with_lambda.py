


my_dict = [
    {"name" : "Nandani", "age" : 23},
    {"name" : "Shagun","age" : 20},
    {"name" : "Ramesh","age" : 21},
    {"name" : "Paresh","age" : 21},
    {"name" : "Babu","age" : 30}
          ]
#this will sort based on age but if age is same of two individuals then what? se below
sorted_list = sorted(my_dict,key= lambda i:i["age"])

print(sorted_list,"\n")



#this will check if age is same then based on name it'll sort
sorted_list = sorted(my_dict,key = lambda a : (a["age"],a["name"]))

print(sorted_list)