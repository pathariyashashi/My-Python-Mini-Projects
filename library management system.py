class Book:
     def __init__(self,book_id,name,quantity):
         self.id = book_id
         self.name= name
         self.quantity=quantity
         self,borrowed_by=[]
         
class User:
    def __init__(self,user_id,name):
         self.id = user_id
         self.name= name
         self,borrowed_books=[]
         
class Admin:
    def __init__(self):
     self.books=[]
     self.users=[]
   
    def add_book(self):
        book_id=int(input("plese enter the book id :"))
        name=input("plese enter the book nmae :")
        quantity=int(input("plese enter the book quantity :"))
        book =  book(book_id,name,quantity)
        self.books.append(book)
        print("\n No books added successfully1:")
    def print_books(self):
      if len(self.books)==0:
          print("\n No books available.\n")
          return
      print("\n Library books:\n")
      for book in self.books:
          print(f"Book ID:{book.id}")  
          print(f"Book NAME:{book.name}")  
          print(f"AVILABLE QUANTITY:{book.quantity}")  
          print("-"*30)  
          
    def  print_books_by_prefix(self):
        prefix=input("enter book prefix:").lower()
        found=False
        for book in self.books:
          if book.name.lower().startswith(prefix):
              print(f"\n{book.name}(ID:[books.id])")
              found=True
          if not found:
              print("\n No books found.\n")  
              
    def add_user(self):
        user_id=int(input("plese Enter user id:")) 
        name=input("plese Enter user name:")       
        
        user= User(user_id,name)
        self.users.append(user) 
        print("\n user added succesfully!\n")
 
    def borrow_books(self):
        user_name = input("plese Enter user name:")
        book_name = input("plese Enter book name:") 
        user =None
        book=None 
        for u in self.users:   
            if u.name.lower()==user_name.lower():
             user = u
            break
        for b in self.books:   
            if b.name.lower()==book_name.lower():
             book = b
            break
        if user is None:
            print("\n user not found.\n")
            return
        if book is None:
            print("\n book not found.\n")
            return
        if book.quantity==0:
            print("\n no copys available.\n")
            return