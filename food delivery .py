class Food:
    def __init__(self,food_id,name,price):
        self.food_id=food_id
        self.name =name
        self.price =price
        
    def __str__(self):
        return f"{self.name}-RS {self.price}"
class Order:
    def __init__(self):
        self.items=[]
        
    def add_food(self,food):
        self.items.append(food)
        print(f"{food.name} added to order:")
        
    def view_order(self):
        print("\n-------- YOUR ORDER ---------")
        if len(self.items) == 0:
            print("No food items!")
        else:
            for items in self.items:
                print(items)
    
    def calculate_bill(self):
        total =0 
        for item in self.items:    
            total += item.price
            print(f"\n Total Bill: RS {total}")     
    
    def track_delivery(self):
        print("\n Order Status:")    
        print("Food is being prepared:")       
        print("Delivery pattern assigned:")
        print("Order outof delivery:") 
        print("Delivered succesfully:")
        
f1=Food(1,"burger",120)   
f2=Food(2,"Pizza",55)
f3=Food(3,"Pasta",40)          
f4=Food(4,"Cold Drink",20)

print("-----MENU-----")

print(f1)
print(f2)
print(f3)
print(f4)

order1=Order()
order1.add_food(f1)
order1.add_food(f2)
order1.add_food(f4)

order1.calculate_bill()
order1.track_delivery