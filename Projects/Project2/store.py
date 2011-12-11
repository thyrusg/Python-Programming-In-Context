class Store:

    def __init__(self):
        self.phones = []
        self.num_of_phones = 0

    def add_quantity(self, amount):
        """Update the amount of phones in the store"""
        self.num_of_phones += amount

    def remove_quantity(self, amount):
        """Remove amount from number of phones"""
        self.num_of_phones -= amount

    def list_phones(self):
        print("%s \t %s \t %s \t %s" %
        ("Manufacturer", "Model", "Price", "Amount"))
        for item in range(0, len(self.phones)):
            print("%s \t %s \t %s \t %s" %
            (self.phones[item][0], self.phones[item][1], self.phones[item][2],
            self.phones[item][3]))

    def add_phone(self):
        """Add phones to the store. Add a way to check if phone is in store"""
        newPhone = []  # List containing the phones data
        manufacturer = input("Enter the name of the manufacturer: ")
        model = input("Enter the model: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        if len(self.phones) == 0:
            newPhone.append(manufacturer)
            newPhone.append(model)
            newPhone.append(price)
            newPhone.append(quantity)
            self.phones.append(newPhone)
            self.add_quantity(quantity)
        elif len(self.phones) > 0:
            for item in range(0, len(self.phones)):
                if manufacturer and model in self.phones[item]:
                    print("That phone is already in the store")
                    print("The extra quantity was added to the phone")
                    self.phones[item][3] += quantity
                    self.add_quantity(quantity)
                    break
                elif manufacturer and model not in self.phones[item]:
                    newPhone.append(manufacturer)
                    newPhone.append(model)
                    newPhone.append(price)
                    newPhone.append(quantity)
                    self.phones.append(newPhone)
                    self.add_quantity(quantity)
                    break
                else:
                    pass

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
                    self.remove_quantity(self.phones[item][3])
                    self.phones.remove(self.phones[item])
                    print("The phone was succesfully removed")
                    #self.remove_quantity(self.phones[item][3])
                    break
                else:
                    print("The phone was not removed")
            else:
                pass

    def get_number_of_phones(self):
        """Return the amount of phones in the store"""
        print(self.num_of_phones)
        return self.num_of_phones

    def update_phone_info(self):
        """Update a phone's information"""
        print("Which phone would you like to update: ?")
        manufacturer = input("Enter manufacturer: ")
        model = input("Enter the model name: ")
        for item in range(0, len(self.phones)):
            if manufacturer and model in self.phones[item]:
                print("What would you like to update: ?")
                answer = int(input("[1] Update manufacturer \n"
                "[2] Update Model \n"
                "[3] Update Price \n" "[4] Update Quantity \n" "[5] Exit \n"))
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
                    originalQuantity = self.phones[item][3]
                    if originalQuantity < newQuantity:
                        self.add_quantity(newQuantity - originalQuantity)
                    elif originalQuantity > newQuantity:
                        self.remove_quantity(originalQuantity - newQuantity)
                    self.phones[item][3] = newQuantity
                elif answer == 5:
                    break
            else:
                pass

    def writer(self):
        f = open(input("Enter the output files name: "), 'w')
        print("Writing the phone data to file")
        for item in range(0, len(self.phones)):
            f.write("%s \t %s \t %s \t %s \n" %
            (self.phones[item][0], self.phones[item][1], self.phones[item][2],
            self.phones[item][3]))
        print("Writing complete \n")
        f.close()

    def importer(self):
        f = open(input("Enter the name of the file: "), 'r')
        print("Reading data")
        for aline in f:
            split = aline.split()
            split[2] = float(split[2])
            split[3] = int(split[3])
            self.add_quantity(split[3])
            self.phones.append(split)
        print("Reading complete \n")
        f.close()
