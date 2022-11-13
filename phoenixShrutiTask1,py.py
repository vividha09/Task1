class librarysys:
    d1={}
    books=['ikigai','silentpateint','python','java']
    def __init__(s,allbooks,library_name):
        s.books=['ikigai','silentpateint','python','java']  
    def add(s,name):
        if(name in s.books):
            print("already exists")
        else:
            print("Added")
            s.books.append(name)    
    def lend(s,name,yrname):
        if(name in s.books):
            s.d1[name]=yrname
            print("The book is lend to ",s.d1)
            s.books.remove(name)
        else:
            print("book is lend to",s.d1[name])
    def returnbk(s,name,yrname):
        if(name in s.d1):
            print(yrname,"book returned")
            s.d1.pop(name)
            s.books.append(name)
        else:
          s.add(name) 
    def display(s,allbooks):
        print("total books:" ,s.books) 
def lib():
    books=['ikigai','silentpateint','python','java']
    obj=librarysys(books,"lib")
    while(True):
        print("1.Display all the books")
        print("2.Add book")
        print("3.Issue book")
        print("4.Return book")
        print("5.Exit")
        c=int(input("Enter"))
        if(c==1):
            obj.display(books)
        elif(c==2):
            name=input("enter book name ")
            obj.add(name)
        elif(c==3):
            yrname=input("enter your name ")
            bname=input("enter the book to lend ")
            obj.lend(bname,yrname)     
        elif(c==4):
            rname=input("enter your name ")
            rbname=input("enter the book to return ")
            obj.returnbk(rbname,rname)     
        elif(c==5):
            print("Exit")    
        else:
            print("Invalid choice")
lib()
