class library:
    dict1={}
    khushi_library=['It ends with us','Harry Potter','Wimpy Kid']
    def __init__(s,allbooks,library_name):
        s.khushi_library=['It ends with us','Harry Potter','Wimpy Kid']  

    def add_book(s,name):
        if(name in s.khushi_library):
            print("book already exists")
        else:
            print("Added!")
            s.khushi_library.append(name) 

    def lend_book(s,name,yourname):
        if(name in s.khushi_library):
            s.dict1[name]=yourname
            print("The book is lend to ",s.dict1)
            s.khushi_library.remove(name)
        else:
            print("book is lend to",s.dict1[name])

    def return_book(s,name,yourname):
        if(name in s.dict1):
            print(yourname,"book returned")
            s.dict1.pop(name)
            s.khushi_library.append(name)
        else:
          s.add_book(name) 

    def display_book(s,allbooks):
        print("total books:" ,s.khushi_library) 


def lib():
    khushi_library=['It ends with us','Harry Potter','Wimpy Kid']
    obj=library(khushi_library,"lib")
    while(True):
        print("1.Display all the khushi_library")
        print("2.Add book")
        print("3.Issue book")
        print("4.Return book")
        print("5.Exit")
        option=int(input("Enter"))
        if(option==1):
            obj.display_book(khushi_library)
        elif(option==2):
            name=input("enter book name ")
            obj.add_book(name)
        elif(option==3):
            yourname=input("enter your name ")
            bookname=input("enter the book to lend_book ")
            obj.lend_book(bookname,yourname)     
        elif(option==4):
            rname=input("enter your name ")
            rbname=input("enter the book to return ")
            obj.return_book(rbname,rname)     
        elif(option==5):
            print("End")    
        else:
            print("Invalid choice")
lib()
