import random
options=["snake","water","gun"]
computer = random.choice(options)
user = input("enter your choice (snake,water,gun)")
").lower()"
print("computer chose:",computer)
print("you chose:",user)
if user == computer:
   print("MATCH DRAW")
elif(user=="snake"and computer=="water")or\
    (user=="water"and computer=="gun")or\
    (user=="gun"and computer=="snake"):
 print("you win")
elif user in options:
    print("you lose")
else:
    print("INVALID input")