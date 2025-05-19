bedtime = input("What time do you want to go to bed? (hh:mm) ")
wake_time = input("What time do you want to wake up? (hh:mm) ") 
age = int(input("How old are you? "))
if age < 18:
    sleep_time = 9 
elif age < 65:
    sleep_time = 8 
else:
    sleep_time = 7 
print("You should sleep for {} hours.".format(sleep_time))

    