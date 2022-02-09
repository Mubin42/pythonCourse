total = int(576)
ls = []
#100 Taka
temp = int(total/100)
total = total % 100
ls.append(temp)
#50 Taka
temp = int(total/50)
total = total % 50
ls.append(temp)
#20 Taka
temp = int(total/20)
total = total % 20
ls.append(temp)
#10 Taka
temp = int(total/10)
total = total % 10
ls.append(temp)
#5 Taka
temp = int(total/5)
total = total % 5
ls.append(temp)
#2 Taka
temp =  int(total/2)
total = total % 2
ls.append(temp)
#1 Taka
ls.append(total)

print(ls[0], "notes of 100 Taka")
print(ls[1], "notes of 50 Taka")
print(ls[2], "notes of 20 Taka")
print(ls[3], "notes of 10 Taka")
print(ls[4], "notes of 5 Taka")
print(ls[5], "notes of 2 Taka")
print(ls[6], "notes of 1 Taka")