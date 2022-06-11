''' This module, librarian.py is a module which contains the functions that are restricted to some users.
    Can only be accessed by librarian with the password.'''

import constants as con


# This function adds the new book with all details in book text file
def add_book(book, author, quantity, price):
    con.book_file()
    # Calculating the untaken id for new book
    book_id = int(max(con.bookDict)+1)
    with open("Book List.txt", "a") as y:
        y.writelines(f"{book_id}\t{book}\t{author}\t{quantity}\t{price}\n")
    # Updating the variable bookDict of constants.py with new book details
    con.bookDict.update({book_id: [book, author, quantity, price]})
    print("Book has been added to the Library.")


# This funtion also adds the book but, which are already in the library.   
def increase_book(book_id, quantity):
    con.particular_list
    con.book_file()
    # Checks if the book ID is in the library and increases the stock of book
    if book_id in con.bookDict.keys():
        particular_list = con.bookDict.get(book_id)
        particular_list[2] = particular_list[2] + quantity
        con.bookDict[book_id] = particular_list
        file = open("Book List.txt","w")
        file.close
        with open("Book List.txt","w") as x:
            for key, value in con.bookDict.items():
                x.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
        print("The quantity of book has been increased by ", quantity)
    else:
        print("Book with this id does not exist.")


# This function removes the book from library
def remove_book(book, quantity):
    con.particular_list
    con.book_file()
    if book in con.bookDict.keys():
        particular_list = con.bookDict.get(book)
        # If book is in the stock, remove the book by given quantity
        if particular_list[2] >=1:
            particular_list[2] = particular_list[2] - quantity
            # After decrease, if stock is less than zero, adds the decreased stock and gives error message.
            if particular_list[2] < 0:
                particular_list[2] = particular_list[2] + quantity
                print("Error! - Number of books you want to remove is less than available books.")
            # After decrease, if stock is greater than zero, updates the book text file with new stock
            elif particular_list[2] > 0:
                con.bookDict[book] = particular_list
                file = open("Book List.txt","w")
                file.close
                with open("Book List.txt","w") as x:
                    for key, value in con.bookDict.items():
                        x.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
                print("Book removed successfully.")
            # After decrease, if stock is equal to zero, erase the records of book from text file.
            elif particular_list[2] == 0:
                con.bookDict.pop(book)
                file = open("Book List.txt","w")
                file.close
                with open("Book List.txt","w") as y:
                    for key, value in con.bookDict.items():
                        y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
                print("All books for this ID has been removed.")
        else:
            print("Book is already removed.")
    else:
        print("The book ID has not been assigned to any of the books")
