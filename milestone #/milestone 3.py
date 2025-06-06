
#set the score to 0
score = 0  
# Define lists of good and bad comments
Good_Comments = ["Good job", "Well done", "Excellent work", "Keep it up", "Great job"]
Bad_Comments = ["Try harder", "You can do better", "Don't give up, Keep practicing", "Don't lose hope"] 
# This program is a simple quiz that tests the user's knowledge on various topics.
print("Welcome to the General Knowledge Quiz!")
# Ask if the user is ready to start the quiz
start = input("Are you ready to start the quiz? (yes/no) ").strip().lower()

if start != "yes":
    print("Okay, maybe next time.")
    exit()  # Stop the program entirely 

print("Great! Let's get started.")

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
if score == 3:
    print("You are a genius!") 
elif score == 2: 
    print("You did great!") 
elif score == 1: 
    print("You did okay, but you can do better.") 
else: 
    print("You need to study more.")
