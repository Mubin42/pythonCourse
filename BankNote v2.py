notesize = [100,50,20,10,5,2,1]
total = int(input("Input Total: "))
noterequired = []

for i in notesize:
    noterequired.append(int(total/i))
    total = total % i

print(noterequired)

for i in range(0,7):
    print(f'{noterequired[i]} notes of {notesize[i]} Taka')