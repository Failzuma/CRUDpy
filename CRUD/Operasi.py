import time
from . import Database
from .Util import random_string

def create(year,title,author):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("An error occured, please try again")

def create_first_data():
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

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Try again")

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("ERROR READING DATABASE")
        return False
