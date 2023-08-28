#  Operator Overriding
# magical methods

# reason behind using this __add__ method  is that for
# doing addition of two object we can not directly use + sing song 
# for changing the functionality of the + sign i created and used __add__ here
# after that + sign will work as we wanted 

"""
followings are the different Magic methods for  arithmatic operators

+ ---> __add__(self,other)
- ---> __add__(self,other)
* ---> __add__(self,other)
/ ---> __add__(self,other)
%---> __add__(self,other)
// ---> __add__(self,other)       
** ---> __add__(self,other)       return a to the power b, for a and b numbers.
@ ---> __matmul__(self,other)     matrix multipiction available from version 3.5
 
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #overriding magic method
    def __add__(self,other):
        return self.x + other.x, self.y + other.y

p1 = Point(1,2)
p2 = Point(3,4)

print(p1+p2)