from project2 import *
from store import *
import sys

# print("Type main() to start the program")


def main():
    myStore = Store()
    print("Welcome to Cellular Solutions")
    print('\n [1] Add Phone \n [2] Remove Phone \n [3] Update Phone Information \n [4] Check Quantity \n [5] Exit \n')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        myStore.add_phone()
    elif choice == 2:
        myStore.remove_phone()
    elif choice == 3:
        myStore.update_phone_info()
    elif choice == 4:
        myStore.get_number_of_phones()
    elif choice == 5:
        sys.exit()
    else:
        main()

if __name__ == "__main__":
    main()
