class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return f'{cls(store.name).name} - franchise'
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f'{store.name}, total stock price: {int(store.stock_price())}'
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


store_one = Store('Test')
store_two = Store('Amazon')
store_two.add_item('keyboard', 160)

print(Store.franchise(store_one))
print(Store.franchise(store_two))

print(Store.store_details(store_one))
print(Store.store_details(store_two))