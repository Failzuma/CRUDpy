import enum
from . import Operasi

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
    title = "title"
    author = "author"
    year = "year"

    # HEADER
    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {author:40} | {year:5}")
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
