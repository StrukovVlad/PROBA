
def piki(func):
    def wrapper(num):
        print("Argument for",func.__name__, "is", num)
        return func(num)
    return wrapper

@piki
def alff(num):
    return num+1
print( alff(1))

