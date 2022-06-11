''' This module, display.py is a module which contains functions that are used only for the purpose of displaying
    the details in the application.'''

import constants as con


#  Function for displaying  the details of books.
def display_books():
    # Calling the function from constans.py
    con.book_file()
    print("---------------------------------------------< Display Book > ---------------------------------------------")
    print(f"Book ID\tTitle\t\t\tAuthor\t\t\tQuantity\tPrice (in $)")
    print("-------------------------------------------------------------------------------------------------------------------------")
    for key, value in con.bookDict.items():
        print(f"{key}\t{value[0]}\t\t\t{value[1]}\t\t{value[2]}\t{value[3]}\n")
   

# Function for displaying the details of lenders in brief.  
def display_lenders():
    con.lender_file()
    print("------------------------------< Display Lenders > ------------------------------")
    print(f"Book\t\tLender\t\tReturn Date")
    print("----------------------------------------------------------------------------------")
    for key, value in con.lenderDict.items():
        print(f"{key[0]}\t\t{key[1]}\t\t{value}\n")

