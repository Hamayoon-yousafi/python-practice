minutes = []
seconds = []

import math
while True: 
    user_input = input("Please Enter mins and secs. ")
    if user_input == "quit":
        break 
    mins, secs = user_input.split()
    minutes.append(int(mins))
    seconds.append(int(secs))    

total_minutes = sum(minutes)
total_seconds = sum(seconds)
total_seconds_in_minutes = total_seconds / 60
total_course_length = total_minutes + total_seconds_in_minutes 
print(f"course is {round(total_course_length/60, 2)} hours long.") 
