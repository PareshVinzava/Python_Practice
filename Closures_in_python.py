# Closures Example


def logger(func):
    def log_func(*args):  # it will takes argumemnts
        print(func(*args)) # and pass arguments here in function

    return log_func     # here i created closure

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)


add_logger(3,4)
add_logger(3,1)
add_logger(5,5)
add_logger(8,4)