class Point:
    def __init__(self, a: int, b: int):
        self.x = a
        self.y = b

p1 = Point(10, 10)
p2 = Point(5, 4)

print(p1.x)
print(p2.x)

class Student:
    def __init__(self, id: int, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname


student1 = Student(1, "Giuseppe", "Gelfusa")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def compute_area(self):
        return self.width * self.height
    
    def __repr__(self):
        return "pipo"

rec1 = Rectangle(10, 3)
print(rec1)