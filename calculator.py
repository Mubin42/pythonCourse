def printing(value):
    print("Answer:", value)

def add(a,b):
    temp = a + b
    printing(temp)

def sub(a,b):
    temp = a - b
    printing(temp)

def mult(a,b):
    temp = a * b
    printing(temp)

def div(a,b):
    temp = a / b
    printing(temp)


x = float(input("First Number: "))
y = float(input("Second Number: "))
while(True):
    mode = str(input(f'''The Numbers are {x} and {y}
Type "add" for Addition
Type "sub" for Subtraction
Type "mult" for Multiplication
Type "div" for Division
Type "cng" for Changing Numbers
Type "q" for Quit
---------------------------------
    '''))
    if(mode == "q"):
        break
    elif(mode == "add"):
        add(x,y)
    elif(mode == "sub"):
        sub(x,y)
    elif(mode == "mult"):
        mult(x,y)
    elif(mode == "div"):
        div(x,y)
    elif(mode == "cng"):
        x = float(input("First Number: "))
        y = float(input("Second Number: "))