def printing(value):
    print("Answer:", value)

#lambda functions
add = lambda a,b: a+b
sub = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b


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
        temp = add(x,y)
        printing(temp)
    elif(mode == "sub"):
        temp = sub(x,y)
        printing(temp)
    elif(mode == "mult"):
        temp = mult(x,y)
        printing(temp)
    elif(mode == "div"):
        temp = div(x,y)
        printing(temp)
    elif(mode == "cng"):
        x = float(input("First Number: "))
        y = float(input("Second Number: "))