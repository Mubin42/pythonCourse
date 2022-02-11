def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def absolute(a,b):
    return abs(a - b)

def power(a,b):
    return pow(a, b)


x = float(input("First Number: "))
y = float(input("First Number: "))
print(add(x,y))
print(sub(x,y))
print(mult(x,y))
print(div(x,y))
print(absolute(x,y))
print(power(x,y))
