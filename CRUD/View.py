import enum
from . import Operasi

def update_console():
    read_console()
    while(True):
        print("Please choose the number book to be updated: ")
        noBook = int(input("Choose the book you want to update: "))
        bookData = Operasi.read(index=noBook)
        if bookData:
            break
        else:
            print("Book not found, please input the number properly")
    break_data = bookData.split(",")
    pk = break_data[0]
    date_add = break_data[1]
    author = break_data[2]
    title = break_data[3]
    year = break_data[4][:-1]
    print(pk)
    print(date_add)
    print(title)
    print(author)
    print(year)

    while(True):
        print("\n"+"="*100)
        print("Input the data you want to update: ")
        print(f"Title\t: {title:.40}")
        print(f"Author\t: {author:.40}")
        print(f"Year\t: {year:4}")

        user_option = input("Choose [1], [2], [3]: ")
        match user_option:
            case "1": # Title
                title = input("Input new title\t: ")
            case "2": # Author
                author = input("Input new author\t: ")
            case "3": # Year
                while True:
                    try:
                        year = int(input("Input new year\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("Year must be 4 digits (yyyy)")
                    except:
                        print("Year must be an integer, please input it properly (yyyy)")
                break
            case _:
                print("The number you input is not valid, please input it properly")
        
        is_done = input("Done already? (y/n): ")
        if is_done in ['y', 'Y']:
            break
    Operasi.update(noBook,pk,date_add,title,author,year)

def create_console():
    print("\n\n"+"="*100)
    print("Input book data")
    author = input("Author\t: ")
    title = input("Title\t: ")
    while True:
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("Year must be 4 digits (yyyy)")
        except:
            print("Year must be an integer, please input it properly (yyyy)")
    Operasi.create(year,title,author)
    print("\nHere's the data")
    read_console()

def read_console():
    data_file = Operasi.read()

    index = "No"
    author = "Author"
    title = "Title"
    year = "Year"

    # HEADER
    print("\n"+"="*100)
    print(f"{index:4} | {author:40} | {title:40} | {year:5}")
    print("-"*100)

    #DATA
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        title = data_break[2]
        author = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {author:.40} | {year:4}",end="")

   
    # FOOTER
    print("="*100+"\n")
