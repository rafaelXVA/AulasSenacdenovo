def h24(x):
    hour,minute,y = x[:-5], x[3:5], x[5:]
    hour = int(hour)
    minute = int(minute)
    if y == "AM":
        if hour == 12:
            hour = 0 
    elif y == "PM":
        if hour != 12:
            hour += 12 
    return f"{hour:02d}:{minute:02d}"
x = "02:30 PM"
print(h24(x))  