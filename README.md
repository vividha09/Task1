# Task1
Linux and python basics




Make a directory names with djs_phoenix_{dir.number}. 
eg:djs_phoenix_1,djs_phoenix_2 etc.

Create 2 more directories inside the same folder.(name convention is same as above)
make 2 files in the 2nd folder named as you know. (your_name_{file.num})
eg: khushi_1,khushi_2 etc.

move the 2nd file in to the third folder


locate the 2nd file.

delete the third directory

From the second file:
1.change the permissions such that everyone can execute. 
2.Inside the second file 

Library Mangement System <br/>
create a library class <br/>
Methods<br/> 1. all_books_display  [a list of books that is there in the library]<br/> eg[Rich_dad , Poor_dad]<br/>
        2. addbook(donate)    [update the list of books if someone comes to donate, if the book is already there in the library print('Book is already there in our library') means the list should have all the distinct books]<br/>  eg[Rich_dad , Poor_dad , Geaography]<br/>
        3. lend book (maintain a dictionary in which , which book has been taken and by whom record should be there,  and all_book_display method should remove that following book)<br/>
        eg {Rich dad: Isha}
        and list will be [Poor dad ,geography]<br/>
        if Vividha ask that I want RIchDad book and if the book has not return by Isha then it should print("Book has been taken by Lisha")<br/>
        4. return book.   (all_books_display list should update if the book is returned and from dictonary also it should get roemoved.)<br/>
        eg: {} empty dict since Isha has returned the book
        updated_list
        [PoorDad,Geography,RichDad]<br/>
        
        
        
// Hint
Create a constructor inside the class which takes the list_of_books and library_name<br/>
eg:<br/>
Khushi_Library=Library();<br/>
KhushiLibrary=Library(listofbooks,libraryname) <br/> 

create a main function  and run an infinite while loop asking users for their input . <br/>
If pressed 1 then addbook method should run.<br/> 
If pressed 2. lend book <br/>
If pressed 3. return book <br/>
If pressed 4. display_book <br/>
If pressed q for quit<br/>
