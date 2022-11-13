class library_management_system:
    khushi_library=['richdad','poordad','geography']
    dict1={}
    def __init__(self,listofbooks,library_name):
        self.khushi_library=['richdad','poordad','geography']
        
    def all_book_display(self,listofbooks):
        print("total books:" ,self.khushi_library)
    def add_book(self,bookname):
        
        if(bookname in self.khushi_library):
            print("Book exists")
        else:
            print("thank you for donating")
            self.khushi_library.append(bookname)
        
       
    def lend_book(self,bookname,name):
        if(bookname in self.khushi_library):
            self.dict1[bookname]=name
            print("The books issued ",self.dict1)
            self.khushi_library.remove(bookname)
        else:
            print("book is taken by ",self.dict1[bookname])
            
        
        
       
    def return_book(self,bookname,name):
       
        
        if(bookname in self.dict1):
            
            print(name,"thank you for returning the book")
            self.dict1.pop(bookname)
            self.khushi_library.append(bookname)
        else:
          self.add_book(bookname)

      
def lib():
    khushi_library=['richdad','poordad','geography']
    obj=library_management_system(khushi_library,"Khushi")
    while(True):
        print("WELCOME TO LIBRARY MAMANGEMENT SYSTEM")
        print("enter 1. to display all books")
        print("enter 2. to add books")
        print("enter 3. to issue books")
        print("enter 4. to return book")
        print("enter 0 to quit")

        a=int(input("select a choice="))
        if(a==1):
            
            obj.all_book_display(khushi_library)
        elif(a==2):
            bookname=input("enter the name of the book ")
            obj.add_book(bookname)
        elif(a==3):
            name=input("Enter your name ")
            bname=input("Enter the book you wanna issue from the list ")
            obj.lend_book(bname,name)
        elif(a==4):
            rname=input("Enter your name ")
            rbname=input("Enter the book you wanna return from the list ")
            obj.return_book(rbname,rname)
        elif(a==0):
            print("thank you for visiting")
            quit()
        else:
            print("Invalid choice")
lib()

  




























































































































































