class Store ():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}

    def add_prod (self, item_name, price):
        self.items[item_name]=price

    def delet_prod (self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price (self, item_name, new_price):
        if item_name in self.items :
            self.items[item_name]=new_price
store1 = Store(name="Магазин 1", adress="Улица 1, 1")
store1.add_prod("яблоки", 0.5)
store1.add_prod("бананы", 0.75)

store2 = Store(name="Магазин 2", adress="Улица 2, 2")
store2.add_prod("хлеб", 1.0)
store2.add_prod("молоко", 0.9)

store3 = Store(name="Магазин 3",adress= "Улица 3, 3")
store3.add_prod("сахар", 1.5)
store3.add_prod("соль", 0.2)


