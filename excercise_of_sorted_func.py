# count which word how many times repeated and return as a dictionary

para = "Python is a high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a \"batteries included\" language due to its comprehensive standard library."


count_dict = {}

for word in para.split():
    if word in count_dict:
        count_dict[word] = count_dict[word] + 1
    else:
        count_dict[word] = 1  

# Syntax: sorted(iterable  (here we have to give iterable), key, reverse)
sorted_list = sorted(count_dict.items(),key = lambda a:a[0])  #always remember if we want to sort dictionary then we have to provide tuple or kind of pairs so for getting pair as tuple we have to use .items() 

print(sorted_list)

