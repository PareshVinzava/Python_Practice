 # Tuple packing and unpackuing 
"""
immutable
defined by parenthesis
"""
#Tuple pakcing
tuplee = (1,2,3,4)
print(tuplee)

#tuple unpacking 
tuplee = (1,2,3,4)

(a,b,c,d) = tuplee #
p,q,r,s = tuplee   #  both with and without parenthisis unpacking is valid

print(a)
print(b)
print(c)
print(d)
print()
print(p)
print(q)
print(r)
print(s)

output = a,b,r,s #tuple packing # this syntax will give tuple containing elements
print(output)