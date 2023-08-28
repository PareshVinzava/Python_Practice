
import pickle

# below function is for dumping data
def storedata():
    #intializing data to be stored in db
    omkar = {"key" : "omkar", "name": "omkar pathak", "age" : 21 , "pay" : 40000} 
    jagdish = {"key" : "jagdish" , "name" : "jagdish pathak" , "age" : 50 , "pay" : 50000}

    # database 

    db = {}
    db["omkar"] = omkar
    db["jagdish"] = jagdish

    #it's important to use binary mode
    dbfile = open("examplepickle","ab")


    # source, destination 
    pickle.dump(db,dbfile)
    dbfile.close()

#below function is for loading the data
def loaddata():
    #for reading also binary mode is important
    dbfile = open("examplepickle","rb")

    #source,destination 
    db = pickle.load(dbfile)

    for keys in db:
        print(keys,"=>" ,db[keys])
    dbfile.close()


# i have created functions so for if i want it to work  then i have to call the both the functions
storedata()
loaddata()

