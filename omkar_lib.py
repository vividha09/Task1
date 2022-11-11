class library_management_system:
    khushi_library=["The_Alchemist", "Intelligent_Investor", "Do_Epic_Shit"]
    dict1={}

    def __init__(self, listofbooks, library_name):
        self.khushi_library=["The_Alchemist", "Intelligent_Investor", "Do_Epic_Shit"]

    def all_book_display(self, listofbooks):
        print("Books in Library:",self.khushi_library)

    def add_book(self, book_name):
        if(book_name in self.khushi_library):
            print("Book already exists in our library.")
        else:
            print("Thank you for donating ",book_name," book")
            self.khushi_library.append(book_name)

    def lend_book(self, book_name, name):
        if(book_name in self.khushi_library):
            self.dict1[book_name]=name
            print("The book issued",self.dict1)
            self.khushi_library.remove(book_name)
        else:
            print("The book is taken by",self.dict1[book_name])

    def return_book(self, book_name, name):
        if(book_name in self.dict1):
            print("Thank you",name,"for returnig the book")
            self.dict1.pop(book_name)
            self.khushi_library.append(book_name)
        else:
            self.add_book(book_name)

def lib():
        khushi_library=["The_Alchemist", "Intelligent_Investor", "Do_Epic_Shit"]
        obj=library_management_system(khushi_library,"Khushi")
        print("WELCOME TO LIBRARY MANAGEMENT SYSTEM !!!")
        while(True):
            print("Enter 1 to add book.")
            print("Enter 2 to issue book.")
            print("Enter 3 to return book.")
            print("Enter 4 to display all books.")
            print("Enter 5 to exit.")

            a=int(input("Enter your choice:"))
            if(a==1):
                book_name=input("Enter the name of book:")
                obj.add_book(book_name)
            elif(a==2):
                name=input("Enter your name:")
                book=input("Enter the book you want to issue:")
                obj.lend_book(book,name)
            elif(a==3):
                rname=input("Enter your name:")
                rbook=input("Enter the book you want to return:")
                obj.return_book(rbook,rname)
            elif(a==4):
                obj.all_book_display(khushi_library)
            elif(a==5):
                quit()
            else:
                print("Invalid choice")
lib()