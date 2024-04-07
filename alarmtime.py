# current time in hour and the hours to wait for the alarm
current_time = int(input("What is the current time in hours? "))
hours_to_wait = int(input("How many hours to wait for the alarm? "))

# calculate the time when the alarm goes off
alarm_time = (current_time + hours_to_wait) % 24

# display the result of the 24 hour clock 
print(f"The alarm will go off at {alarm_time}:00 on a 24-hour clock.")





