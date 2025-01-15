#2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = πr^2. (Use the value 3.14 for π). Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount ofwater in the pond? Print the answer without any decimal point init.
import math
radius=84
pi =3.14
Area_of_circle=pi*radius*radius
print("The Area of circle is:",Area_of_circle)
#Amount of water in the pound per square meter is 1.4 liters
Amount_of_water=1.4
Total_amount_of_water=int(Area_of_circle*Amount_of_water)
print("The total amount of water contained in the pool is:", Total_amount_of_water)
