time = "12:50:45PM"
hour = int(time[:2])

timeformat = str(time[-2:])
if(timeformat == "AM"):
    time = time[0:8]
else:
    if(hour==12):
        hour = 0
    else:
        hour = hour + 12
    time = (str(hour)+ time[2:8])
print(time)