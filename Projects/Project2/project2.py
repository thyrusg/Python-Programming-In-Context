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
