""""
A robot moves in a plane starting from the original point (0, 0).
The robot can move toward up, down, left and right with a given stesp.
The trace of robot movement is hoswn as the following:
  UP 5
  Down 3
  LEFT 3
  RIGHT 2

  The numbers after the direction are steps. Please write a program to compute the distance from current position
  after a sequence of movement and original point. If the distance is a float, hen just print the nearest integer.
"""
from math import sqrt
def euclidean_distance(x1, y1, x2, y2):
    return sqrt(((x1-x2)**2 + (y1-y2)**2))


def update_position(x, y, direction, step):
    if direction == "UP":
        y += step
    elif direction == "DOWN":
        y -= step 
    elif direction == "RIGHT":
        x += step
    else:
        x -= step
    return x, y

def move_robot_from_input():
    x = 0
    y = 0
    order = input("Please enter the direction and step(ex: UP 5): ")
    
    while order != "":
        split_order = order.split(" ")
        direction = split_order[0].upper()
        step = int(split_order[1])
        x, y = update_position(x, y, direction, step)
        
        order = input("Please enter the direction and step(ex: UP 5): ")
    
    return euclidean_distance(0, 0, x, y)

    

print(move_robot_from_input())
