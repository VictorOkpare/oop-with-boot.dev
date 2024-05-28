# import csv

# class Tshirts:
#     all = []
#     def __init__(self, product: str, brandname: str, colour: str, size: str, quantity: int ):
#         assert quantity >= 0, f"Your order {quantity}pcs is not up to 1pc "
#         self.product = product
#         self.brandname = brandname
#         self.colour = colour
#         self.size = size
#         self.quantity = quantity
        
#         Tshirts.all.append(self)   

#     def cost(self):
#         price = 0
#         if self.brandname == "Kanin":
#             price = 1500 * self.quantity
#         elif self.brandname == "Goldstar":
#             price = 1600 * self.quantity
#         elif self.brandname == "Airpilot":
#            price = 1450 * self.quantity
#         elif self.brandname == "SMT":
#             price = 1800 * self.quantity
#         else:
#             print("This brandname is not available")
#         return price
    

    
#     @classmethod
#     def instance_from_csv(cls):
#         with open('tshirts.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             tshirts = list(reader)
#             for tshirt in tshirts:
#                 cls(
#                     product=tshirt.get('product'),
#                     brandname=tshirt.get('brandname'),
#                     colour=tshirt.get('colour'),
#                     size=tshirt.get('size'),
#                     quantity=int(tshirt.get('quantity', 0))
#                 )
#             print(tshirt)
#     def __repr__(self):
     
#         return f"Tshirts({self.product}, {self.brandname}, {self.colour}, {self.size}, {self.quantity})"
# print(Tshirts.instance_from_csv())
# print(Tshirts.all)




    # @classmethod
    # def instance_from_csv(cls):
    #        with open ('tshirts.csv', 'r') as f:
    #         reader = csv.DictReader(f)
    #         tshirts = list(reader)
    #         for tshirt in tshirts:
    #             tshirt(
    #                 product = tshirt.get('product'),
    #                 brandname = tshirt.get('brandname'),
    #                 colour = tshirt.get('colour'),
    #                 size = tshirt.get('size'),
    #                 quantity =tshirt.get('quantity')
    #             )
    #             print(tshirt)

import csv

class Tshirts:
    all = []
    
    def __init__(self, product: str, brandname: str, colour: str, size: str, quantity: int):
        assert quantity >= 0, f"Your order {quantity}pcs is not up to 1pc "
        self.product = product
        self.brandname = brandname
        self.colour = colour
        self.size = size
        self.quantity = quantity
        
        Tshirts.all.append(self)   

    def cost(self):
        price = 0
        if self.brandname == "Kanin":
            price = 1500 * self.quantity
        elif self.brandname == "Goldstar":
            price = 1600 * self.quantity
        elif self.brandname == "Airpilot":
           price = 1450 * self.quantity
        elif self.brandname == "SMT":
            price = 1800 * self.quantity
        else:
            print("This brandname is not available")
        return price

    @classmethod
    def instance_from_csv(cls):
        with open('tshirts.csv', 'r') as f:
            reader = csv.DictReader(f)
            tshirts = list(reader)
            for tshirt in tshirts:
                cls(
                    product=tshirt.get('product'),
                    brandname=tshirt.get('brandname'),
                    colour=tshirt.get('colour'),
                    size=tshirt.get('size'),
                    quantity=int(tshirt.get('quantity', 0))
                )
                print(tshirt)

    def __repr__(self):
        return f"Tshirts({self.product}, {self.brandname}, {self.colour}, {self.size}, {self.quantity})"
    def search_availability_by_brandname(self, brandname):
        for order in all:
            if brandname == self.brandname:
                print(order)
            else:
                print("This order was not taking")
                

# Populate instances from the CSV file
# Tshirts.instance_from_csv()

# Print all instances
#

