def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    if y == 0:
        raise ValueError("Divide by 0 exception")
    return x//y