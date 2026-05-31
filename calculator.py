def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return"error:cannot divide by zero"
    return a/b

while True:
    print("\n=====CALCULATOR=====")
    print("1.addition(+)")
    print("2.subtraction(-)")
    print("3.multiplication(*)")
    print("4.division(/)")
    print("5.EXIT")
    
    choice=input("enter your choice (1-5):")
    if choice=="5":
        print("calculator CLOSE.....")
        break
    try:
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
    except:
        print("invalid input! plese enter numbers only.")
        continue
    if choice=="1":
        print("result:",add(num1,num2))
    elif choice=="2":
        print("result:",sub(num1,num2))
    elif choice=="3":
        print("result:",mul(num1,num2))
    elif choice=="4":
        print("result:",div(num1,num2))
    else:
        print("invalid choice! plese select between 1-5.")
    