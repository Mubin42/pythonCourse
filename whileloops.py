i = 1
ls = []
while(i<=10): #only to include values in list
    ls.append(i)
    i += 1 #i = i + 1
print(ls)

sum = 0
i = 0
while(i<10):
    sum = sum + ls[i]
    i += 1
print(sum)
