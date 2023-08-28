def take_seccond(elem):
    return elem[1]

random = [(2,20),(3,40),(4,10),(1,13)]
#here we created on function which will take the second elem of tuple if list
#and in sorted function will return sorted output according to the second value of tuple 
sorted_list = sorted(random,key=take_seccond)
print(sorted_list)

#example i have list containig tuples of name, mark and age 
#so i have to sort them as per highest mark to lowest mark 
# and if marks are same then accroding to age using function and sorted function

participat_list = [

    ("rakesh",78,20),
    ("mahesh",90,19),
    ("shagun",95,22),
    ("meet",80,25),
    ("jay",90,26)
]   

def sorter(item):  #sorted will take this function in place of key = 
    s_marks = 100-item[1]  #this will give subtraction from 100 so the lowest value will be first
    age = item[2]   #this will help to sort when marks are same 
    return s_marks,age

sorted_list2 =sorted(participat_list,key=sorter)  # in sorted function first we have to give what we want to sort then in place of key= our function on based on what we want to sort

print(sorted_list2)