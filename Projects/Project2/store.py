class Store:

    def __init__(self):
        self.phones = []
        self.num_of_phones = 0

    def update_quantity(self, amount):
        """Update the amount of phones in the store"""
        self.num_of_phones += amount

    def add_phone(self):
        """Add phones to the store. Add a way to check if phone is in store"""
        newPhone = []
        manufacturer = input("Enter the name of the manufacturer: ")
        newPhone.append(manufacturer)  # Index is 0
        model = input("Enter the model: ")
        newPhone.append(model)  # Index is 1
        for item in range(0, len(self.phones)):
            if manufacturer and model in self.phones[item]:
                print("That phone is already in the store")
                break
            else:
                pass
        price = int(input("Enter the price: "))
        newPhone.append(price)  # Index is 2
        quantity = int(input("Enter the quantity: "))
        newPhone.append(quantity)  # Index is 3
        self.phones.append(newPhone)
        self.update_quantity(quantity)

    def remove_phone(self):
        """Remove phone from the store"""
        manufacturer = input("Enter the manufacturer: ")
        model = input("Enter the model: ")
        for item in range(0, len(self.phones)):
            if manufacturer and model in self.phones[item]:
                answer = input("Are you sure ? (Y/N)")
                if answer == 'y' or 'Y':
                    print("%s %s %s %s" % (self.phones[item][0],
                    self.phones[item][1], self.phones[item][2],
                    self.phones[item][3]))
                    self.phones.remove(self.phones[item])
                    print("The phone was succesfully removed")
                else:
                    print("The phone was not removed")
            else:
                pass

    def get_number_of_phones(self):
        """Return the amount of phones in the store"""
        return self.num_of_phones

    def update_phone_info(self):
        """Update a phone's information"""
        print("Which phone would you like to update: ?")
        manufacturer = input("Enter manufacturer: ")
        model = input("Enter the model name: ")
        for item in range(0, len(self.phones)):
            if manufacturer and model in self.phones[item]:
                print("What would you like to update: ?")
                answer = int(input("[1] Update manufacturer \n",
                "[2] Update Model \n,"
                "[3] Update Price \n", "[4] Update Quantity \n", "[5] Exit"))
                if answer == 1:
                    newManu = input("Enter the new manufacturer: ")
                    self.phones[item][0] = newManu
                elif answer == 2:
                    newModel = input("Enter the new model: ")
                    self.phones[item][1] = newModel
                elif answer == 3:
                    newPrice = int(input("Enter the new price: "))
                    self.phones[item][2] = newPrice
                elif answer == 4:
                    newQuantity = int(input("Enter the new quantity: "))
                    self.phones[item][3] = newQuantity
                elif answer == 5:
                    break
