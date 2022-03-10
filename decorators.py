def sub(func):
    def insert(a,b):
        print("first executed")

        value = func(a,b)
        print("final execution")
        return value
    return insert
@sub
def subract(a,b):
    print("second executed")
    return a - b

print(subract(10,5))
