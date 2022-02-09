try:
    num = int(input("Number"))
    print(10/num)
except ValueError:
    print("Value Mismatch")

except ZeroDivisionError:
    print("Not possible to divide by 0")
