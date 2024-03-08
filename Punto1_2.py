import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle1:
    def __init__(self, width, height, bottom_left_corner_x, bottom_left_corner_y):
        self.width = width
        self.height = height
        self.bottom_left_corner = Point(bottom_left_corner_x, bottom_left_corner_y)
    
    def compute_area(self):
        return self.width * self.height
    
    def compute_perimeter(self):
        return 2 * (self.width + self.height)
    
    def compute_interference_point1(self, point):
        if (self.bottom_left_corner.x <= point.x <= self.bottom_left_corner.x + self.width) and \
           (self.bottom_left_corner.y <= point.y <= self.bottom_left_corner.y + self.height):
            return "The point is inside the rectangle."
        else:
            return "The point is not inside the rectangle."

class Rectangle2(Rectangle1):
    def __init__(self, width, height, center_point_x, center_point_y):
        self.width = width
        self.height = height
        self.center_point = Point(center_point_x, center_point_y)

    def compute_interference_point2(self, point):
        if (self.center_point.x <= point.x <= self.center_point.x + self.width) and \
           (self.center_point.y <= point.y <= self.center_point.y + self.height):
            return "The point is inside the rectangle."
        else:
            return "The point is not inside the rectangle."

class Rectangle3(Rectangle1):
    def __init__(self, bottom_x, bottom_y, upper_x, upper_y):
        self.bottom_left_corner = Point(bottom_x, bottom_y)
        self.upper_right_corner = Point(upper_x, upper_y)

    def compute_width_height(self):
        if self.bottom_left_corner.x == self.upper_right_corner.x and self.bottom_left_corner.y == self.upper_right_corner.y:
            return "It's a point."
        else:
            self.width = abs(self.bottom_left_corner.x - self.upper_right_corner.x)
            self.height = abs(self.bottom_left_corner.y - self.upper_right_corner.y)
            return self.width and self.height

    def compute_interference_point3(self, point):
        if (self.bottom_left_corner.x <= point.x <= self.bottom_left_corner.x + self.width) and \
           (self.bottom_left_corner.y <= point.y <= self.bottom_left_corner.y + self.height):
            return "The point is inside the rectangle."
        else:
            return "The point is not inside the rectangle."

class Square(Rectangle1):
    def __init__(self, width):
        self.width = width
        self.height = width

#Below the initializing of a rectangle using the first method.
interference_point1 = Point(-1, -1)
rectangle1 = Rectangle1(2, 2, 0, 0)
area1 = rectangle1.compute_area()
perimeter1 = rectangle1.compute_perimeter()
interference_result1 = rectangle1.compute_interference_point1(interference_point1)

print("Method 1:")
print(f"The rectangle's area is {area1}")
print(f"The rectangle's perimeter is {perimeter1}")
print(interference_result1)
print("-----------------------------------------------------------------------")

#Below the initializing of a rectangle using the second method.
interference_point2 = Point(-8.5, -6.7)
rectangle2 = Rectangle2(3, 3, 1, 1)
area2 = rectangle2.compute_area()
perimeter2 = rectangle2.compute_perimeter()
interference_result2 = rectangle2.compute_interference_point2(interference_point2)

print("Method 2:")
print(f"The rectangle's area is {area2}")
print(f"The rectangle's perimeter is {perimeter2}")
print(interference_result2)
print("-----------------------------------------------------------------------")

#Below the initializing of a rectangle using the third method.
interference_point3 = Point(-10, 30)
rectangle3 = Rectangle3(-1, -1, 8, 4)
atributes = rectangle3.compute_width_height()
area3 = rectangle3.compute_area()
perimeter3 = rectangle3.compute_perimeter()
interference_result3 = rectangle3.compute_interference_point3(interference_point3)

print("Method 3:")
print(f"The rectangle's area is {area3}")
print(f"The rectangle's perimeter is {perimeter3}")
print(interference_result3)
print("-----------------------------------------------------------------------")

#Below the initializing of a square.
square = Square(3)
area4 = square.compute_area()
perimeter4 = square.compute_perimeter()

print(f"The square's area is {area4}")
print(f"The square's perimeter is {perimeter4}")