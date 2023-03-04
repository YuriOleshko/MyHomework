class Item:

    def __init__(self, name, price, dimensions, description):
        self.name = name
        self.price = price
        self.dimensions = dimensions
        self.description = description

    def __str__(self):
        return f'{self.name}, price: {self.price}$'

class User:

    def __init__(self, name, surname, numberphone, balance):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}, has on the balance sheet {self.balance}$'

class Purchase:

    def __init__(self, user):
        self.user = user
        self.products = {}
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        item_str = '\n'.join([f'{item.name}: {cnt}' for item, cnt in self.products.items()])
        return f'User: {self.user.name} {self.user.surname}\nItem:\n{item_str}\nTotal cost: {self.get_total()}$'

    def get_total(self):
        self.total = sum([item.price * cnt for item, cnt in self.products.items()])
        if self.total <= self.user.balance:
            return self.total
        else:
            return f'On the balance of {self.user.balance} dollars and you need {self.total}'


lemon = Item('lemon', 5, 'small', 'small',)
apple = Item('apple', 2, 'red', 'middle', )
print(lemon)
print(apple)

buyer = User('Ivan', 'Ivanov', '02628162', 150)
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert cart.get_total() == 60
print('OK')