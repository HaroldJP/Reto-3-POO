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
