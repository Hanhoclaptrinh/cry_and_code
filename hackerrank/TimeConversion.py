def timeConversion(s):
    hour=int(s[:2])
    rest=s[2:8]
    period=s[8:]
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{rest}"