score = 0 
Good_Comments = ["Good job", "Well done", "Excellent work", "Keep it up", "Great job"]
Bad_Comments = ["Try harder", "You can do better", "Don't give up, Keep practicing", "Don't lose hope"]
# This program is a simple quiz that tests the user's knowledge on various topics.
print("Welcome to the General Knowledge Quiz!")
# This program will test your knowledge on various topics. 
input("Are you ready to start the quiz? (yes/no) ")
# This input is used to determine if the user is ready to start the quiz    
if input("Are you ready to start the quiz? (yes/no) ") == "yes":
    print("Great! Let's get started.")
else:
    print("Okay, maybe next time.") 

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print(Good_Comments[0])  # Randomly selected good comment 
    print("Paris is the capital of France.")  
    score += 1
else:
   print(Bad_Comments[0])  # Randomly selected bad comment
    # Randomly selected bad comment
   print("Incorrect. The capital of France is Paris.") 
answer = input("What is the largest planet in our solar system? ") 
if answer.lower() == "jupiter":
   print(Good_Comments[0]) 
   print("Correct! Jupiter is the largest planet in our solar system.")  
   score += 1 
else: 
    print("Incorrect. The largest planet in our solar system is Jupiter.")   
    print(Bad_Comments[0])
answer = input("how many continents are there on Earth? ") 
if answer == "7":
    print("Correct! There are 7 continents on Earth.")  
    print(Good_Comments[0])  
    score += 1 
else:
    print("Incorrect. There are 7 continents on Earth.") 
    print(Bad_Comments[0]) 

print("Your final score is: {}/3".format(score))
print("Thank you for playing the quiz!")
