
#set the score to 0
score = 0  
wrong1 = 0 
wrong2 = 0 
wrong3 = 0
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
# Loop through each question until the correct answer is given

# Question 1
while True:
    answer = input("What is the capital of France? ")
    if answer.lower() == "paris":
        print(Good_Comments[0])
        print("Paris is the capital of France.")
        score += 1
        break
    else:
        print(Bad_Comments[0])
        print("Incorrect. The capital of France is Paris. Try again.")
        wrong1 = 1

# Question 2
while True:
    answer = input("What is the largest planet in our solar system? ")
    if answer.lower() == "jupiter":
        print(Good_Comments[0])
        print("Correct! Jupiter is the largest planet in our solar system.")
        score += 1
        break
    else:
        print(Bad_Comments[0])
        print("Incorrect. The largest planet in our solar system is Jupiter. Try again.")
        wrong2 = 1
# Question 3
while True:
    answer = input("how many continents are there on Earth? ")
    if answer == "7":
        print("Correct! There are 7 continents on Earth.")
        print(Good_Comments[0])
        score += 1
        break
    else:
        print(Bad_Comments[0])
        print("Incorrect. There are 7 continents on Earth. Try again.") 
        wrong3 = 1
# Final score and feedback 
totalwrong = wrong1 + wrong2 + wrong3 
if totalwrong == 0: 
    print("Congratulations! You answered all questions correctly.") 
elif totalwrong == 1: 
    print("You got 1 question wrong. Keep practicing!") 
elif totalwrong == 2: 
    print("You got 2 questions wrong. Don't give up, keep trying!") 
elif totalwrong == 3: 
    print("You got all questions wrong. Don't lose hope, keep practicing!")  
print(f"Your final score is: {score} out of 3") 



