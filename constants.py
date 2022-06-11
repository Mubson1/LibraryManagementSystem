''' This module, constants.py is a module which contains some  functions and variables which are being constantly
    used in other modules.'''


from datetime import datetime, date

# A function which returns the current date.
def getDate():
    Date = date.today()
    return Date


# A function which returns the current time.
def getTime():
    time = datetime.today()
    return  str(time.strftime("%H:%M:%S"))


''' This process of opening book text file and keeping each word in a list is repeated in various modules.
    So, this process is made a function and is called throughout the module.'''
def book_file():
    book_file.bookList = []
    book_file.bookDict = {}
    #Opening  the text file where records of book are kept
    bookFile = open("Book List.txt", "r")
    for line in bookFile:
        eachLine = line.strip()
        lineList = eachLine.split('\t')
        book_file.bookList.append(lineList)
    bookFile.close()
    i = 0
    while i < len(book_file.bookList):
        try:
            #Keeping list itself as a value of dictionary
            book_file.bookDict.update({int(book_file.bookList[i][0]):[book_file.bookList[i][1],book_file.bookList[i][2],
            int(book_file.bookList[i][3]), book_file.bookList[i][4]]})
        except:
            print("List is empty")
        i += 1    


''' This process of opening summarized lender text file and keeping each word in a list is repeated in various modules.
    So, this process is made a function and is called throughout the module.'''
def lender_file():
    lender_file.lenderList = []
    lender_file.lenderDict = {}
    #Opening  the text file where records of lenders are kept in brief
    lenderFile = open("Summarized Lender List.txt", "r")
    for line in lenderFile:
        eachLine = line.strip()
        lineList = eachLine.split('\t')
        lender_file.lenderList.append(lineList)
    lenderFile.close()
    i = 0
    while i < len(lender_file.lenderList):
        try:
            # Making touple of bookID, lender as key of the dictionary and returnDate as value
            lender_file.lenderDict.update({(int(lender_file.lenderList[i][0]),lender_file.lenderList[i][1]) : lender_file.lenderList[i][2]})      
        except:
            print("Lender List is empty")
        i += 1


# This is just an empty list which is called in various functions of other modules.
particular_list = []

''' Dictionary and list of book_file and lender_file are used in many modules for update, pop or delete.
    So, those values are stored in each of the following variables and are called whenever necessary'''
book_file()
bookDict = book_file.bookDict
bookList = book_file.bookList

lender_file()
lenderDict = lender_file.lenderDict
lenderList = lender_file.lenderList





