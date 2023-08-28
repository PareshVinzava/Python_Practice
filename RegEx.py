# RegEx
import re

# META Characters are [],^,$,*,+,?,{},(),\,|

pattern = '^a...s$'
test_string = 'abyss'

result = re.match(pattern,test_string)

if result:
    print("search successful.")
else:
    print("search unsuccessful")


pattern = '^a...s$'
test_string = 'abbbyss'

result = re.match(pattern,test_string)

if result:
    print("search successful.")
else:
    print("search unsuccessful")


# if abc exits or not in string

stri = "tebde def rgt h uj yuntrhb"

result = re.match(r"[abc]",stri)
print(result)  #gives none because it only check at starting of string and stops at space

#now use re.search instead of re.match

stri = "tebde def rgt h uj yuntrhb"

result = re.search(r"[abc]",stri)
print(result)

#find all each and every place what found

stri = "tebde def rgt h uj yuntrhb"

result = re.findall(r"[abc]",stri)
print(result)

# period any single character  except /n  (.. two char, ... three char)

print(re.search(r"..",'abc'))


#  ^  caret 
# if string starts with a certain character.

print(re.search(r'^a','a'))
print(re.search(r'^ab','ab'))
print(re.search(r'^ab','acb')) #gives none coz not match first two char

#dollar sybl $
# checks ends with char or not


#star * 
# this matches zero or more occurrences of the pattern left to it.

print(re.search(r'ma*n','mn'))  #n must followed by a if a avilable

# pluse +
# one or more occurrences , at least one occurrences
# match after..


print(re.search(r'ma+n','mn'))
print(re.search(r'ma+n','woman'))


#question mark ma?n
# {} braces


print(re.search(r'aP{2,3}','abc dat'))




