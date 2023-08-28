# deserialization or unpickle

# Deserialization / Unpickle / load

import pickle

f = open("pickled.txt","rb")

d = pickle.load(f) #here i am unpickled the pickle file using load 

print(d)

f.close()