def sheesh(hour12h):
    hour, minute1 = hour12h.split(":")
    minute, periodo = minute1[:2], minute1[3:]
    hour = int(hour)
    minute = int(minute)
    if periodo == "AM":
        if hour == 12:
            hour = 0 
    elif periodo == "PM":
        if hour != 12:
            hour += 12  
    return f"{hour:02d}:{minute:02d}"


hour12h = "04:30 PM"
print(sheesh(hour12h))  