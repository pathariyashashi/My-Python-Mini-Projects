tasks =[]

while True:
   
    print("\n----TO DO LIST----")
    print("1. view task")
    print("2.add task")
    print("3.delete task")
    print("4.exit")
    
    Choice = input("enter your choice:")
    if Choice=="1":
        if len(tasks)==0:
            print("no task found!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
                
    elif Choice=="2":
        tasks = input("enter new task:")
        tasks.append(tasks) 
        print("task added!") 
        
    elif Choice =="3":
        if len(tasks)==0:
            print("no task to delete!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
                num =int(input("enter task number to delete:"))
                if 0<num<=len(tasks):
                    tasks.pop(num-1)
                    print("task deleted!")
                else:
                    print("invalid number!")
    elif Choice=="4":
                    print("goodby!")
                    break
    else:
        print("invalid choice")
                    
                              