#using the __init__ function
class market:
    def __init__(self, name, price):
        self.name = name
        self.price = price

rice = market("rice", "900frs")

print(rice.price + " is for one and half kilo" ) 