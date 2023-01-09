import time
from . import Database
from .Util import random_string
import os

def delete(noBook):
    try:
        with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
            data = file.readlines()
            data.pop(noBook-1)
            file.seek(0)
            file.writelines(data)
            file.truncate()
    except:
        print("Error while deleting")

def update(noBook,pk,date_add,title,author,year):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'
    
    data_length = len(data_str)
    
    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(data_length*(noBook-1))
            file.write(data_str)
    except:
        print("Error while updating")
def create(year,title,author):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'
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

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Try again")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            book_amount = len(content)
            if "index" in kwargs:
                indexBook = kwargs["index"]-1
                if indexBook < 0 or indexBook > book_amount:
                    return False
                else:
                    return content[indexBook]
            else:
                return content
    except:
        print("Error reading database")
        return False
