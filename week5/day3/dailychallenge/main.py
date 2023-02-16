import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified.")
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value
        self._diameter = value * 2
        self._area = math.pi * value ** 2
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive.")
        self._diameter = value
        self._radius = value / 2
        self._area = math.pi * (value / 2) ** 2
    
    @property
    def area(self):
        return self._area
    
    def __str__(self):
        return f"Circle with radius {self.radius:.2f}"
    
    def __repr__(self):
        return f"Circle({self.radius:.2f})"
    
    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
c1 = Circle(radius=5)
print(c1.radius)    # 5
print(c1.diameter)  # 10
print(c1.area)      # 78.53981633974483
print(c1)           # Circle with radius 5.00

c2 = Circle(diameter=10)
print(c2.radius)    # 5
print(c2.diameter)  # 10
print(c2.area)      # 78.53981633974483
print(c2)           # Circle with radius 5.00

c3 = c1 + c2
print(c3.radius)    # 10
print(c3.diameter)  # 20
print(c3.area)      # 314.1592653589793
print(c3)           # Circle with radius 10.00

print(c1 == c2)     # True
print(c1 < c2)      # False

circles = [c1, c3, c2]
circles.sort()
print(circles)      # [Circle(5.00), Circle(5.00), Circle(10.00)]
