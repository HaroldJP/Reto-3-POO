# Reto-3-POO

## Punto 1:

Create a repo with the class exercise.

* Create class Line.

```python
import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def compute_length(self):
        length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return length
    
    def compute_slope(self):
        if self.x2 - self.x1 == 0 and self.y2 - self.y1 == 0: 
            return print("Es un punto.") 
        elif self.x2 - self.x1 == 0:
            return print("Indeterminado.")
        
        slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        return slope
    
    def compute_horizontal_cross(self):
        return self.y1 == 0 or self.y2 == 0
    
    def compute_vertical_cross(self):
        return self.x1 == 0 or self.x2 == 0

linea = Line(3, 4, 3, 4)
print("Longitud:", linea.compute_length())
print("Pendiente:", linea.compute_slope())
print("Intersección eje X:", linea.compute_horizontal_cross())
print("Intersección eje Y:", linea.compute_vertical_cross())
```

* Redefine the class Rectangle, adding a new method of initialization using 4 Lines (composition at its best, a rectangle is compose of 4 lines).

```python
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.line_start = Point(x1, y1)
        self.line_end = Point(x2, y2)

class Rectangle:
    def __init__(self, *args):
        self.width = args[0]
        self.height = args[1]
        self.bottom_left_corner = Point(args[2], args[3])
        self.center_point = Point(args[4], args[5])
        self.upper_right_corner = Point(args[6], args[7])
        self.line_1 = Line(args[8], args[9], args[10], args[11])
        self.line_2 = Line(args[12], args[13], args[14], args[15])
        self.line_3 = Line(args[16], args[17], args[18], args[19])
        self.line_4 = Line(args[20], args[21], args[22], args[23])
    
    def compute_area(self):
        return self.width * self.height
    
    def compute_perimeter(self):
        return 2 * (self.width + self.height)
    
    def compute_interference_point(self, point, method):
        if method == 1:
            if (self.bottom_left_corner.x <= point.x <= self.bottom_left_corner.x + self.width) and \
               (self.bottom_left_corner.y <= point.y <= self.bottom_left_corner.y + self.height):
                return True
            else:
                return False
        elif method == 2:
            if (self.center_point.x - self.width/2 <= point.x <= self.center_point.x + self.width/2) and \
               (self.center_point.y - self.height/2 <= point.y <= self.center_point.y + self.height/2):
                return True
            else:
                return False
        elif method == 3 or method == 4:
            if (self.bottom_left_corner.x <= point.x <= self.upper_right_corner.x) and \
               (self.bottom_left_corner.y <= point.y <= self.upper_right_corner.y):
               return True
            else:
                return False

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(args[0], args[0], *args[1:])

def initialization_rectangle(method):
    method = int(input("Enter the method to initialize the rectangle (1, 2, 3, 4): "))
    if method == 1:
        width = float(input("Enter the rectangle's width: "))
        height = float(input("Enter the rectangle's height: "))
        x = float(input("Enter the x coordinate for the rectangle's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the rectangle's bottom-left corner: "))
        rectangle = Rectangle(width, height, x, y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    elif method == 2:
        width = float(input("Enter the rectangle's width: "))
        height = float(input("Enter the rectangle's height: "))
        x = float(input("Enter the x coordinate for the rectangle's center point: "))
        y = float(input("Enter the y coordinate for the rectangle's center point: "))
        rectangle = Rectangle(width, height, 0, 0, x, y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    elif method == 3:
        x1 = float(input("Enter the x coordinate for the rectangle's bottom-left corner: "))
        y1 = float(input("Enter the y coordinate for the rectangle's bottom-left corner: "))
        x2 = float(input("Enter the x coordinate for the rectangle's upper-right corner: "))
        y2 = float(input("Enter the y coordinate for the rectangle's upper-right corner: "))
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        rectangle = Rectangle(width, height, x1, y1, 0, 0, x2, y2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    elif method == 4:
        print("Now you're going to create a rectangle using lines,")
        print("you need to enter the first line's starting point and")
        print("ending point. Then, the first line's ending point")
        print("will be the second line's starting point, and the")
        print("second line's ending point will be the third line's")
        print("starting point. Finally, the first line's starting")
        print("point will be the fourth's line starting point,")
        print("and the third's ending will be the fourth's ending.")
        x1_line_1 = float(input("Enter the x coordinate for the first line starting point: "))
        y1_line_1 = float(input("Enter the y coordinate for the first line starting point: "))
        x2_line_1 = float(input("Enter the x coordinate for the first line ending point: "))
        y2_line_1 = float(input("Enter the y coordinate for the first line ending point: "))
        x_line_2 = float(input("Enter the x coordinate for the second line ending point: "))
        y_line_2 = float(input("Enter the y coordinate for the second line ending point: "))
        x_line_3 = float(input("Enter the x coordinate for the third line ending point: "))
        y_line_3 = float(input("Enter the y coordinate for the third line ending point: "))
        width = abs(x1_line_1 - x_line_2)
        height = abs(y1_line_1 - y_line_2)
        rectangle = Rectangle(width, height, x1_line_1, y1_line_1, 0, 0, x_line_2, y_line_2, x1_line_1, y1_line_1, x2_line_1, y2_line_1, x2_line_1, y2_line_1, x_line_2, y_line_2, x_line_2, y_line_2, x_line_3, y_line_3, x_line_3, y_line_3, x1_line_1, y1_line_1)
        
        #if (x2_line_1 != x_line_2) or (x1_line_1 != x_line_3) or (y_line_2 != y_line_3) or (x_line_3 != x1_line_1):
            #print("That's not a rectangle.")
        #else:
    print("Area:", rectangle.compute_area())
    print("Perimeter:", rectangle.compute_perimeter())

    point_x = float(input("Enter the x coordinate of the point: "))
    point_y = float(input("Enter the y coordinate of the point: "))
    point = Point(point_x, point_y)
    interference = rectangle.compute_interference_point(point, method)
    if interference == True:
        print("The point is inside the rectangle.")
    else:
        print("The point is not inside the rectangle.")

def initialization_square(method):
    method = int(input("Enter the method to initialize the square: "))
    if method == 1:
        width = float(input("Enter the square's width: "))
        height = width
        x = float(input("Enter the x coordinate for the square's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the square's bottom-left corner: "))
        square = Square(width, height, x, y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    elif method == 2:
        width = float(input("Enter the square's width: "))
        height = width
        x = float(input("Enter the x coordinate for the square's center point: "))
        y = float(input("Enter the y coordinate for the square's center point: "))
        square = Square(width, height, 0, 0, x, y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    elif method == 3:
        x1 = float(input("Enter the x coordinate for the square's bottom-left corner: "))
        y1 = float(input("Enter the y coordinate for the square's bottom-left corner: "))
        x2 = float(input("Enter the x coordinate for the square's upper-right corner: "))
        y2 = float(input("Enter the y coordinate for the square's upper-right corner: "))
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        square = Square(width, height, x1, y1, 0, 0, x2, y2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    if width != height:
        print("That's not a square.")

    else:
        print("Area:", square.compute_area())
        print("Perimeter:", square.compute_perimeter())

        point_x = float(input("Enter the x coordinate of the point: "))
        point_y = float(input("Enter the y coordinate of the point: "))
        point = Point(point_x, point_y)
        interference = square.compute_interference_point(point, method)
        if interference == True:
            print("The point is inside the square.")
        else:
            print("The point is not inside the square.")


if __name__ == "__main__":
    method = int
    initialization_rectangle(method)
    #initialization_square(method)
```

## Punto 2

Restaurant scenario: You want to design a program to calculate the bill for a customer's order in a restaurant.


```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Beverage(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class FastFood(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Lunch(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Protein(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price

if __name__=="__main__":

    coca_cola = Beverage(name="Coca-cola", price=3500, kind = "Cold beverage")
    orange_juice = Beverage(name="Orange juice", price=3000, kind = "Cold beverage")
    lemonade = Beverage(name="Lemonade", price=2500, kind = "Cold beverage")
    water = Beverage(name="Water", price=2000, kind = "Cold beverage")
    coffee = Beverage(name="Coffee", price=2500, kind = "Hot beverage")
    chocolate = Beverage(name="Chocolate", price=2500, kind = "Hot beverage")

    hot_dog = FastFood(name="Hot dog", price=10000, kind = "Big sausace")
    hamburguer = FastFood(name="Hamburguer", price=12000, kind = "Double beef")
    pizza = FastFood(name="Pizza", price=8000, kind = "Extra cheese")

    lentils = Lunch(name="Lentils with rice and salad", price=7000, kind = "Ordinary")
    beans = Lunch(name="Beans with rice and salad", price=7000, kind = "Ordinary")
    pasta = Lunch(name="Pasta with bread and salad", price=6500, kind = "Executive")

    beef = Protein(name="Beef", price=6000, kind = "Cow")
    chicken = Protein(name="Chicken", price=5500, kind = "Chicken meal")
    fish = Protein(name="Mojarra", price=7800, kind = "Fish meal")

    # Enter your order
    your_order = [water, lentils, chicken, pizza]

    order = Order(your_order)

    # Total price
    total_price = order.calculate_total_price()

    print("Order:")
    for item in order.items:
        print(f"- {item.name}: ${item.price}")

    print(f"Total price: ${total_price}")
```

```mermaid
classDiagram
    MenuItem <|-- Lunch
    MenuItem <|-- Fast_food
    MenuItem <|-- Beverage
    MenuItem <|-- Protein
    Order *-- MenuItem
    Order : +String items
    Order : +calculate_total_price()
    MenuItem: +String name
    MenuItem: +int price
    class Lunch{
      +String kind
    }
    class Beverage{
      -String kind
    }
    class Fast_food{
      +String kind
    }
    class Protein {
        -String kind
    }
```
