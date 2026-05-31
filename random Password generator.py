import random
import string
length = (int(input("Entre Password length:")))

all_character=string.ascii_letters + string.digits + string.punctuation

password=""

for i in range(length):
    password += random.choice(all_character)
    
print("Generated Password:",password)    