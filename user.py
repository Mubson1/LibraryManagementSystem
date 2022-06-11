''' This module, user.py is the module which includes  the functions to lend and return book.
    This module is seperated as it performs tasks that are common to all users.'''

import display
import constants as con
from datetime import date,time,datetime,timedelta
import os


# This function handles all the things that happens while lending book.
def lend_book():
    sum_ = 0
    check = "go"
    choice1 = "+"
    # Loop for lending additional books.
    while (choice1 == "+"):
        while True:
            try:
                book = int(input("Enter id of the book you want to lend => "))
                break
            except:
                print("Enter a correct ID")
        # If loop is used so that user name would be needed only once for a particular transaction.
        if(check == "go"):
            user = input("Enter your name => ").upper()
        price = int(con.bookDict[book][3])
        lender_filePath = os.path.abspath("Lender Lists Collection/lender-[ "+user+" ].txt")
        if book in con.bookDict.keys():
            # Book can only be lended if the stock is available
            if con.bookDict[book][2] >= 1:
                lendDate = con.getDate()
                lendTime = con.getTime()
                returnDate = lendDate + timedelta(days = 10)
                # This text file keeps the summary of lender.
                with open("Summarized Lender List.txt", "a") as w:
                    w.writelines(f"{book}\t{user}\t{returnDate}\n")
                con.lenderDict.update({(book, user) : str(returnDate)})
                # This text file keeps the details of lending transaction.
                with open(lender_filePath,"a") as x:
                    if (check == "go"):
                        x.writelines(f"\t Anime World Library \t \n")
                        x.writelines("\t``````````````````````````\n")
                        x.writelines(f"Receive date \t {lendDate}  {lendTime}\n")
                        x.writelines(f"Return date \t {returnDate}\n")
                        x.writelines("\n")
                        x.writelines(f"Name \t\t {user}\n")
                    x.writelines(f"Book \t\t {con.bookDict[book][0]}-[{book}]\n")    
                    x.writelines("----------------------------------------------------------\n")
                    x.writelines(f"You paid \t\t {con.bookDict[book][3]} $ \n")
                    x.writelines(f"============================================== \n\n")
                    sum_ += price
                # Decreasing the stock of book
                particular_list = con.bookDict.get(book)
                particular_list[2] = particular_list[2] - 1
                con.bookDict[book] = particular_list
                file = open("Book List.txt","w")
                file.close
                with open("Book List.txt","w") as y:
                    for key, value in con.bookDict.items():
                        y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
                print(f"{user}, you have successfully lended the book, {con.bookDict[book][0]}.")
                print(f"You have to pay a lending charge of {price}$ for this book.")
            else:
                print("Your search for book is out of stock.")
        else:
            print("Sorry, your search for book is not in our library.")
        print()
        choice1 = input("Press + to lend more books => ")
        check = "stop"
    with open(lender_filePath,"a") as y:
        y.write("Total Price: \t" + str(sum_) + "\n")
        y.write(f"....................................................................................................................................\n\n\n\n\n")
    while(choice1 != "+"):
        print()
        print("Thank you for visiting.")
        break
    

# This function handles returning of book and calculates if  fine is needed to be paid
def return_book(book, user):
    con.particular_list
    lender_filePath = os.path.abspath("Lender Lists Collection/lender-[ "+user+" ].txt")
    returner_filePath = os.path.abspath("Returner Lists Collection/Returner-[ "+user+" ].txt")
    # The book  is only returned if the book has been lended to the user.
    if(book, user) in con.lenderDict.keys():
        returnDate1 = con.lenderDict[(book,user)]
        returnDate2 = datetime.strptime(returnDate1,"%Y-%m-%d")
        returnDate = returnDate2.date()
        lendedDate = returnDate - timedelta(10)
        currentDate = con.getDate()
        currentTime = con.getTime()
        '''Calculating if fine is needed to be paid. If fine is needed to be paid, goes to another
            function payment(book, user). If not, returns book.'''
        if currentDate > returnDate:
            lateDate = (currentDate - returnDate).days
            fine = lateDate*3
            print("You need to pay a fine of ", fine,"$.")
            payment(book, user)
        else:
            # This text file keeps the details of returning transaction
            with open(returner_filePath, "a") as y:
                y.writelines(f"\t Anime World Library \t \n")
                y.writelines("\t``````````````````````````\n")
                y.writelines(f"Returned date \t {currentDate}  {currentTime}\n")
                y.writelines(f"Lended date \t {lendedDate}\n")
                y.writelines("\n")
                y.writelines(f"Name \t\t {user}\n")
                y.writelines(f"Book \t\t {con.bookDict[book][0]}-[{book}]\n")    
                y.writelines("----------------------------------------------------------\n")
                y.writelines(f"Fine paid \t\t  0 $ \n")
                y.writelines(f"........................................................................................................... \n\n\n")
            # Deleting the record of lender only from summarized lender list
            del con.lenderDict[(book,user)]
            file1 = open("Summarized Lender List.txt","w")
            file1.close
            with open("Summarized Lender List.txt","w") as x:
                for key, value in con.lenderDict.items():
                    x.write(f"{key[0]}\t{key[1]}\t{value}\n")
            con.book_file()
            # Increasing the stock of book
            particular_list = con.bookDict.get(book)
            particular_list[2] = particular_list[2] + 1
            con.bookDict[book] = particular_list
            file = open("Book List.txt","w")
            file.close
            with open("Book List.txt","w") as y:
                for key, value in con.bookDict.items():
                    y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")   
            print(f"{user}, thank you for returning the book, {con.bookDict[book][0]} in time.")
    else:
        print("This book has never been issued to your name.")


''' This function is only executed when fine needs to be paid while returning book. Asks options
    whether to pay fine or not immediately.'''
def payment(book, user):
    print("1. Pay fine.")
    print("2. Not now.")
    option = input("Enter your choice => ")
    if option not in["1","2"]:
        print("Please enter a correct option.")
    else:
        option = int(option)
        if option == 1:
            con.particular_list
            lender_filePath = os.path.abspath("Lender Lists Collection/lender-[ "+user+" ].txt")
            returner_filePath = os.path.abspath("Returner Lists Collection/Returner-[ "+user+" ].txt")
            returnDate1 = con.lenderDict[(book,user)]
            returnDate2 = datetime.strptime(returnDate1,"%Y-%m-%d")
            returnDate = returnDate2.date()
            lendedDate = returnDate - timedelta(10)
            currentDate = con.getDate()
            currentTime = con.getTime()
            lateDate = (currentDate - returnDate).days
            fine = lateDate*3
            # Creating a text file with details of transaction
            with open(returner_filePath, "a") as y:
                y.writelines(f"\t Anime World Library \t \n")
                y.writelines("\t``````````````````````````\n")
                y.writelines(f"Returned date \t {currentDate}  {currentTime}\n")
                y.writelines(f"Lended date \t {lendedDate}\n")
                y.writelines("\n")
                y.writelines(f"Name \t\t {user}\n")
                y.writelines(f"Book \t\t {con.bookDict[book][0]}-[{book}]\n")    
                y.writelines("----------------------------------------------------------\n")
                y.writelines(f"Fine paid \t\t  {fine} $ \n")
                y.writelines(f"........................................................................................................... \n\n\n")
            # Deleting the record of lender only in summarized lender list.
            del con.lenderDict[(book,user)]
            file1 = open("Summarized Lender List.txt","w")
            file1.close
            with open("Summarized Lender List.txt","w") as x:
                for key, value in con.lenderDict.items():
                    x.write(f"{key[0]}\t{key[1]}\t{value}\n")
            con.book_file()
            # Increasing the stock of book
            particular_list = con.bookDict.get(book)
            particular_list[2] = particular_list[2] + 1
            con.bookDict[book] = particular_list
            file = open("Book List.txt","w")
            file.close
            with open("Book List.txt","w") as y:
                for key, value in con.bookDict.items():
                    y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")   
            print(f"{user}, thank you for returning the book, {con.bookDict[book][0]}.")
        elif option == 2:
            # If fine is not paid, then takes to display_books function of display.py
            print("We are now redirecting you to our book collections")
            display.display_books()











        
