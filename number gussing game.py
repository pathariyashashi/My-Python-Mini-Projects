import random
number = random.randint(1,100)
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("guess a number between 1 and 100")
attempts=0
while True:
    guess =int(input("enter your guess"))
    attempts += 1
    if guess>number:
       print("TOO HIGH! try Again.") 
    elif guess<number:
       print("TOO LOW! try Again.") 
    else: 
        print("correct guess!")
        print("attemts taken:",attempts)
        break  