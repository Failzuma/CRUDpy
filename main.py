import os
import CRUD as CRUD

if __name__ == "__main__":
    op = os.name

    match op:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("WELCOME TO PROGRAM")
    print("DIGITAL LIBRARY")
    print("====================")

    # CHECK IF DATABASE IS PRESENT
    CRUD.init_console()

    while (True):
        match op:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("WELCOME TO PROGRAM")
        print("DIGITAL LIBRARY")
        print("====================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Pick a number: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("Done already? (y/n): ")
        if is_done in ['y', 'Y']:
            break
    print("Program stopped, thanks for coming by!")
