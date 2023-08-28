# here in this task i have to find the distance according to the movement of the person in differ directions
import math

staring_position = [0,0]
ending_position = [0,0]

actions = [
    ("up",5),
    ("down",1),
    ("left",3),
    ("right",2)
]

for action in actions:

    a = action[0]
    b = action[1]

    if a == "up":
       ending_position[1] = ending_position[1]+b
    elif a == "down":
        ending_position[1] = ending_position[1]-b
    elif a == "left":
       ending_position[0] = ending_position[0]-b
    elif a == "right":
        ending_position[0] = ending_position[0]+b
     
print(ending_position)


def minkowski_distance(staring_position,ending_position,root):  # minkowski is the equation for finding the dictance so i've written that equation in function
    distance = ((ending_position[0]-staring_position[0])**root + (ending_position[1]-staring_position[1])**root)**(1/root)
    return distance

#here i've taken different values for root
root = 1

print(f"Distance for root {root} is {minkowski_distance(staring_position,ending_position,root)}")

root = 2

print(f"Distance for root {root} is {minkowski_distance(staring_position,ending_position,root)}")

root = 3

print(f"Distance for root {root} is {minkowski_distance(staring_position,ending_position,root)}")



