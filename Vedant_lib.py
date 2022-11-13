class library:

    lended = {}
    def __init__(self, list, name):
        self.list = list
    def lendBook(self,bookname,name):
        if bookname in self.list:
            self.lended[bookname]=name
        print("Book is taken by:", self.lended)
        self.list.remove(bookname)
    def addBook(self,newbook):
        self.list.append(newbook)
        print("Thanks for adding")

    def returnBook(self, book):
        self.lended.pop(book)

def main():
    list = ['Power of Your Subconcious Mind', 'Rich Dad Poor Dad',
            'Monk who sold his Ferrari', 'Awaken the Giant within', 'One Thing']
    std = library(list,"Vedant")
    while(True):
        print("Welcome to the Vedant library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Add a Book")
        print("3. Lend a Book")
        print("4. Return a Book")
        print("q to quit")
        choice = input()
        if choice not in ['1','2','3','4','q']:
            print("Enter a valid option")
            continue
        if choice=="q":
            exit()
        else:
            choice = int(choice)
        if choice == 1:
            print("All books list: ")
            for i in list:
                print(i)

        elif choice == 2:
            newbook = input("Enter the name of the book you want to add:")
            std.addBook(newbook)

        elif choice == 3:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            std.lendBook(book, user)

        elif choice == 4:
            book = input("Enter the name of the book you want to return:")
            std.returnBook(book)
            print("Thanks for returning our book safely")
        else:
            break


main()
