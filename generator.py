# generator

def getsequenceupto(x):
    for i in range(x):
        yield i

seq = getsequenceupto(10)

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))  #here it'll stop iteration

