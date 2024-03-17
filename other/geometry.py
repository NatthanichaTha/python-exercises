from __future__ import annotations
import math 

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        
    def compute_len(self):
        len = math.sqrt(( self.p1.x - self.p2.x )**2 + (self.p1.y - self.p2.y)**2)
        return len
    
class Multiline:
    def __init__(self, points: list[Point]):
        self.multiline = points
    def compute_multiline_len(self):
        multiline_len = 0
        for x in range(0, len(self.multiline)-1):
            for y in range(1, len(self.multiline)):
                line = Line(self.multiline[x], self.multiline[y])
                multiline_len += line.compute_len()
        return multiline_len

class Rectangle:
    def __init__(self, topleft: Point, bottomright: Point):
        self.p1 = topleft
        self.p3 = bottomright
        self.p2 = Point(self.p3.x, self.p1.y)
        self.p4 = Point(self.p1.x, self.p3.y)

    def area(self):
        height = Line(self.p1, self.p4)
        width = Line(self.p1, self.p2)
        len_height = height.compute_len()
        len_width = width.compute_len()
        return len_height * len_width
        
    def perimeter(self):
        top_len = Line(self.p1, self.p2).compute_len()
        right_len = Line(self.p2, self.p3).compute_len()
        bottom_len = Line(self.p3, self.p4).compute_len()
        left_len = Line(self.p4, self.p1).compute_len()
        return top_len + right_len + bottom_len + left_len
    
    def intersect(self, rec: Rectangle):
        if rec.p1.x >= self.p2.x:
            #rec is on the right of self
            return False
        if rec.p2.x <= self.p1.x:
            #rec is on the left of self
            return False
        if rec.p3.y <= self.p1.y:
            #rec is above self
            return False
        if rec.p1.y >= self.p3.y:
            #rec is below sef
            return False
        return True

        
if __name__ == "__main__":
    rec1 = Rectangle(Point(0, 0), Point(5, 5))
    rec2 = Rectangle(Point(5.1, 5.1), Point(6, 6))
    print(rec1.intersect(rec2))

