def convert_to_24_hour(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour == 0
    else:
        if hour != 12:
            hour += 12

    return "{:02d}{:02d}".format(hour, minute)
time = convert_to_24_hour(3, 20, "am")
print(time)