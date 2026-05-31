import random
words = ["python","java","code","game"]
word = random.choice(words)

guessed = ["_"]*len(word)
attempts = 6
while attempts>0 and"_"in guessed:
    print("word:","".join(guessed))
    guess =input("enter a letter:").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
    else:
        attemts -=1
        print("wrong guess attemts left:",attempts)
        if "_"not in guessed:
            print("you win! word was:",word)
        else:
            print("you Lose! word was:,word") 