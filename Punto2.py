class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Beverage(MenuItem):
    pass

class FastFood(MenuItem):
    pass

class Lunch(MenuItem):
    pass

class Protein(MenuItem):
    pass

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price

if __name__=="__main__":

    coca_cola = Beverage(name="Coca-cola", price=3500)
    orange_juice = Beverage(name="Orange juice", price=3000)
    lemonade = Beverage(name="Lemonade", price=2500)
    water = Beverage(name="Water", price=2000)
    coffee = Beverage(name="Coffee", price=2500)
    chocolate = Beverage(name="Chocolate", price=2500)

    hot_dog = FastFood(name="Hot dog", price=10000)
    hamburguer = FastFood(name="Hamburguer", price=12000)
    pizza = FastFood(name="Pizza", price=8000)

    lentils = Lunch(name="Lentils with rice and salad", price=7000)
    beans = Lunch(name="Beans with rice and salad", price=7000)
    pasta = Lunch(name="Pasta with bread and salad", price=6500)

    beef = Protein(name="Beef", price=6000)
    chicken = Protein(name="Chicken", price=5500)
    fish = Protein(name="Mojarra", price=7800)

    # Enter your order
    your_order = [water, lentils, chicken, pizza]

    order = Order(your_order)

    # Total price
    total_price = order.calculate_total_price()

    print("Order:")
    for item in order.items:
        print(f"- {item.name}: ${item.price}")

    print(f"Total price: ${total_price}")
