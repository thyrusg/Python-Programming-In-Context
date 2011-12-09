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
        manufacturer = input("Enter the name of the manufacturer ")
        newPhone.append(manufacturer)
        model = input("Enter the model ")
        newPhone.append(model)
        price = int(input("Enter the price"))
        newPhone.append(price)
        quantity = int(input("Enter the quantity"))
        newPhone.append(quantity)
        self.phones.append(newPhone)
        self.update_quantity(quantity)

    def remove_phone(self):
        """Remove phone from the store"""
        manufacturer = input("Enter the manufacturer")
        model = input("Enter the model")
        for item in range(0, len(self.phones)):
            if manufacturer and model in self.phones[item]:
                answer = input("Are you sure ? (Y/N)")
                if answer == 'y' or 'Y':
                    self.phones.remove(self.phones[item])
                else:
                    print("The phone was not removed")
            else:
                print("That phone isn't in the store")
