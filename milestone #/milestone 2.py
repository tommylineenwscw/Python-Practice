# Sleep Calculator 
# This program calculates the amount of sleep you need based on your age and sleep schedule. 
# This input is used to determine ask the user what time they want to go to bed and what time they want to wake up.
bedtime = input("What time do you want to go to bed? (hh:mm) ")
wake_time = input("What time do you want to wake up? (hh:mm) ") 
# This input is used to determine how old the user is
age = int(input("How old are you? "))
# This if elif else statement is used to determine the amount of sleep the user needs based on their age
if age < 18:
    sleep_time = 9 
elif age < 65:
    sleep_time = 8 
else:
    sleep_time = 7 
#end of if elif else statement, and saying how much sleep they need to the user.

print("You should sleep for {} hours.".format(sleep_time)) 
