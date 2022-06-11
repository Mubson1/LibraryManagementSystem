''' This module, main_page.py is a module which is used for running the program.
    This module doesn't have any functions but instead uses functions from all the modules to run the program.'''

import display
import user
import librarian
import constants as con

if __name__ == "__main__":
    while(True):
        try:
            # Things shown at the main page when program is executed.
            print("----------------Welcome to ANIME WORLD library----------------")
            print("1. Display Lists")
            print("2. Lend Book")
            print("3. Return Book")
            print("===========================================")
            print("4. Access as Librarian")
            print("..............................................................................")
            print("5. Exit")
            print()
            
            option2 = input("Enter your choice => ")
            if option2 not in ["1","2","3","4","5"]:
                print("Wrong choice. \n")
                continue
            else:
                option2 = int(option2)
                if option2 == 1:
                    print()
                    print("You are currently at - [DISPLAY BOOK SECTION]")
                    print("1. Book List")
                    print("2. Lender List")
                    option3 = input("Enter you choice => ")
                    if option3 not in ["1","2"]:
                        print("Wrong choice.")
                        continue
                    else:
                        # Shows display of books
                        option3 = int(option3)
                        if option3 == 1:
                            display.display_books()
                        # Shows display of lenders
                        elif option3 == 2:
                            display.display_lenders()
                # Lends the book
                elif option2 == 2:
                    print()
                    print("You are currently at - [LEND BOOK SECTION]")
                    user.lend_book()
                # Returns the book
                elif option2 == 3:
                    print()
                    print("You are currently at - [RETURN BOOK SECTION]")
                    book = int(input("Enter id of the book you want to return => "))
                    name = input("Enter your name => ").upper()
                    user.return_book(book, name)
                # Restriction of special functions to all users. 
                elif option2 == 4:
                    password = input("Enter a password: ")
                    if password == "11":
                        print()
                        print("You are currently at - [LIBRARIAN SECTION]")
                        print("1. Add new book")
                        print("2. Add existing book")
                        print("3. Remove book")
                        print("4. Go back")
                        choice = input("Enter your choice => ")
                        if choice not in ["1","2","3","4"]:
                            print("Wrong choice")
                            continue
                        else:
                            choice = int(choice)
                            # Adds new book  in the library
                            if choice == 1:
                                print()
                                print("You are currently at - [ADD NEW BOOK SECTION]")
                                book =  input("Enter the name of the book => ")
                                author = input("Enter the author name => ")
                                quantity = int(input("Enter the quantity of books => "))
                                price = input("Enter the price for lending the book => ")
                                librarian.add_book(book, author, quantity, price)
                            # Increases the book stock in the library
                            elif choice == 2:
                                print()
                                print("You are currently at - [ADD EXISTING BOOK SECTION]")
                                book_id = int(input("Enter id of the book you want to add => "))
                                quantity = int(input("Enter the number of books to add => "))
                                librarian.increase_book(book_id, quantity)
                            # Removes book from the library
                            elif choice == 3:
                                print()
                                print("You are currently at - [REMOVE BOOK SECTION]")
                                book = int(input("Enter  id of the book you want to remove => "))
                                quantity = int(input("Enter the number of books to remove => "))
                                librarian.remove_book(book, quantity)
                            # Exits the librarian mode and displays the book collection
                            elif choice == 4:
                                print("We are redirecting you to our book collections.")
                                display.display_books()
                    else:
                        print("Wrong password.")
                        continue
                elif option2 == 5:
                    break

                # After every execution of functions, asks user to continue or quit
                print("press [c] to continue and [q] to quit")
                option3 = ""
                while(option3 != "c" and option3 != "q"):
                    print()
                    option3 = input("Enter your choice => ").upper()
                    if option3 == "C":
                        break
                    elif option3 == "Q":
                        exit()
        except:
            print("Please redo the process correctly. Be sure to input the correct data.")
            continue

           
