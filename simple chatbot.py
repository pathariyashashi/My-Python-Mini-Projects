def chatbot():
    print("===SIMPLE-CHATBOT===")
    print("type 'by' to Exit")
    
while True:
    user = input("you:").lower() 
    
    if user=="hello":
        print("bot:Hi there!") 
    elif user=="how are you":
        print("bot:i am fine!")
    elif user=="what is your name":
        print("bot:i am Python chatbot!")
    elif user=="where you locating":
        print("bot:there is no location of my era!")
    elif user=="bye":
        print("bot:GoodBye RAA!")
        continue
    else:
        print('bot:sorry, i dont understand...')
chatbot()       