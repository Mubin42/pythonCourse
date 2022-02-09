time = "11:50:45PM"
hour = int(time[:2])

timeformat = str(time[-2:])
if(timeformat == "AM"):
    time = time[0:8]
else:
    hour = hour + 12
    time = (str(hour)+ time[2:8])
print(time)