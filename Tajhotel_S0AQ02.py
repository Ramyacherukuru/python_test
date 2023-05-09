from math import radians
from math import tan
angle_of_elevation1 = radians(25) 
angle_of_elevation2 = radians(65) 
distance = 100
height = (distance * tan(angle_of_elevation2) - distance * tan(angle_of_elevation1))
distance2 = height / tan(angle_of_elevation2)
print("Height of the Taj Hotel tower :", height ,"yards")
print("distance between Gateway of India and Taj Hotel’s entrance:", distance2, "yards")


