# serialization & deserialization
# pickle module used for it
# write and binary mode opened must
# not human readable 
# Serialize / Pickle / dump


# it is example of serialization or pickle
import pickle

f = open("pickled.txt", "wb")

dct = {"name":"Rajeev","age":23,"Gender":"Male","marks":75}

pickle.dump(dct,f)  # here i am created pickle file using dump it is kmown as dumping.

f.close()

