class Phone:
	def __init__(self, manufactuer, model, price, quantity):
		self.manufact = manufactuer
		self.model = model
		self.price = price
		self.quantity = quantity

	def set_manufact(self, newManfact):
		self.manufact = newManfact

	def set_model(self, newModel):
		self.model = newModel

	def set_retail_price(self, newPrice):
		self.price = newPrice

	def set_quantity(self, newQuantity):
		self.quantity = newQuantity

	def get_manufact(self):
		return self.manufact

	def get_model(self):
		return self.model

	def get_retail_price(self):
		return self.price

	def get_quantity(self):
		return self.quantity

	# To-do: 
	# Create a Store class. 
	# Store should have a list of objects of type Phone
	# An attribute that represents the number of phones.
	# Create a initializer, add_phone, and remove_phone.

class Store:
	def __init__(phones, numOfPhones):
		self.phones = []
		self.numOfPhones = len(self.phones)

	def add_phone(phoneObject):
		if phoneObject in self.phones:
			print("%s is already in the store" % str(phoneObject))
		else:
			self.phones.append(phoneObject)

	def remove_phone(phoneObject):
		phoneModel = input("What model is the phone ?")
		phoneManufact = input("Who manufactured the phone ?")
		if (phoneModel and phoneManufact) in self.phones:
			delete = input("Are you sure you want to delete this phone information from the system ? <Y=Yes/N=No>")
				if delete == "Y" or "y":
					self.phones.remove(phoneObject)
				else:
					pass
		else:
			pass

	def get_number_of_phones(self):
		return self.numOfPhones

	def update_phone_info(self, manufacturer, model):
		print("Chose one of the following options: \n")
		options = input("[1] Update manufacturer\n [2] Update the model\n [3] Update the retail price\n [4] Update the quantity\n [5] exit\n Enter you choice.")
		if options == 1:
			do something
		elif options == 2:
			do something
		elif options == 3:
			do something
		elif options == 4:
			do something
		elif options == 5:
			pass
