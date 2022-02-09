# num = 10
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")
#
# print("Run")

num = int(input("Input Number: "))
if(num==0): #zero er condition
    print("Zero")
else: #zero na howar jonno condition
    if(num%2==1): #odd number jonno condition
        print("Odd")
    else:
        if(2<=num & num<=5):
            print("Even and Between 2 to 5")
        elif(6<=num & num<=20):
            print("Even and Between 6 to 20")
        elif(num>20):
            print("Greater Than 20")
