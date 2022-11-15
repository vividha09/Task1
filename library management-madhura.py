#!/usr/bin/env python
# coding: utf-8

# In[36]:


khushi_library_cr=['Rich dad','Poor dad','geography']
name_renter={}
print("Welcome to Khushi's Library !")
def addbook(newbook):
    khushi_library_cr.append(newbook)
def lend_book(book_to_lend):
    del khushi_library_cr[khushi_library_cr.index(book_to_lend)]
    name_of_renter=input("enter your name")#enter name
    #put in dict
    name_renter[book_to_lend]=name_of_renter
def return_book(book_to_return):
    del name_renter[book_to_return]#del from the rented dictionary
    khushi_library_cr.append(book_to_return)#append to original list
def main():
    while(1):
        ch=input("Please press 1 to add a book\nPlease press 2 to lend a book\nPlease press 3 to return a book\nPlease press 4 to display a book\n\'q\'for Quit\n")
        if (ch=='1'):
            new_book=input("Enter the name of the book to add:- ")
            if not new_book in khushi_library_cr:
                addbook(new_book)
            else:
                print("book already exists in the library!")
        elif (ch=='2'):
            book_to_lend=input("enter the name of the book you want to rent")
            if book_to_lend in khushi_library_cr:
                lend_book(book_to_lend)
            else:
                print("The required book has already been  lent to",name_renter[book_to_lend])
        elif (ch=='3'):
            book_to_return=input("enter the name of the book you want to return-  ")#has to be in the dictionary
            for x in name_renter:
                if book_to_return==x:
                    return_book(book_to_return)
                    break
        elif (ch=='4'):
            print("All books in the library:\n")
            for x in khushi_library_cr:
                print(x)
        else:
            break
main()

    


# In[ ]:




        


# In[ ]:



    

