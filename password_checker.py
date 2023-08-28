# password checker whether it is valid or not 


import re   # this module is used for searching elements faster


passwords = [x for x in input().split(",")]  #here i am taking valuues from the user by saperated by comma

# print(passwords)

values = []

for i in passwords:
    
    if len(i) < 6 or len(i) > 12: # if password id small than 6 or big than 12 that value of i won't be considered and take next i.
        continue
    else:
        pass

    if not re.search("[a-z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif  not re.search("[$#@]",i):
        continue
    elif re.search("\s",i):
        continue
    else:
        pass
    values.append(i) # if value of i satisfied all the conditions then that i is appened to values

    
    
    
print(",".join(values))

    
        