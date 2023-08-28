# Operator Precedence

"""
Lowest
|
| or
| and 
| Not
| ==,!=,<,>.....
| =,-
| *,/,//,%
| **
|
Highest
"""

a =20 + 5*2 - 25
print(a)

b = 20+5**2.6/2
print(b)

season = "summer"
age = 10
colour = "pink"
if season == "summer" or age > 0 and colour  == "pink":
    print("ok")
else:
    print("not ok")