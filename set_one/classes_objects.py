class Store:
    # You'll need 'name' as an argument to this method.
    # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    def __init__(self, name):
        self.name = name
        self.items = []

    # Create a dictionary with keys name and price, and append that to self.items.
    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    # Add together all item prices in self.items and return the total.
    def stock_price(self):
        return sum([itemus['price'] for itemus in self.items])


item = Store('Donald')

item.add_item('hot-dog', 34)
item.add_item('candy', 23)
item.add_item('headphones', 53)

print(item.stock_price())
