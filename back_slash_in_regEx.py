import re
#  \ in regEx


# \A  

print(re.findall(r'\Athe','the telegram'))

# \b

print(re.findall(r'\bfoo','football'))

# \b

print(re.findall(r'\Bfoo','football'))

# \d any digits 0 to 9

print(re.findall(r'\d','football12'))

# \D non digitals

print(re.findall(r'\D','football123'))

# \s any whitespace chara

print(re.findall(r'\s','foot ball'))

# \S non whitespace char

print(re.findall(r'\S','foot ball'))

# \w  alfanumeric character 

print(re.findall(r'\w','foot ball12'))

# \W  non - alfanumeric character

print(re.findall(r'\W','foot ball12@'))

# \Z specific character at only at end od string

print(re.findall(r'12\Z','foot ball12'))
 

