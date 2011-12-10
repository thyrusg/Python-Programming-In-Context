import project2
import store
import sys

# print("Type main() to start the program")

myStore = store.Store()


def main():
    print("Welcome to Cellular Solutions")
    print('''
    [1] Add Phone
    [2] Remove Phone
    [3] Update Phone Information
    [4] Check Quantity
    [5] List Phones
    [6] Import Data
    [7] Save Data
    [8] Exit''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        myStore.add_phone()
        main()
    elif choice == 2:
        myStore.remove_phone()
        main()
    elif choice == 3:
        myStore.update_phone_info()
        main()
    elif choice == 4:
        myStore.get_number_of_phones()
        main()
    elif choice == 5:
        myStore.list_phones()
        main()
    elif choice == 6:
        myStore.importer()
        main()
    elif choice == 7:
        myStore.writer()
        main()
    elif choice == 8:
        sys.exit()

if __name__ == "__main__":
    main()
