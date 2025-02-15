import math

Numofsides = int(input('Input number of sides:'))
LengthofSides = int(input('Input the length of a side:'))

P = Numofsides * LengthofSides

apothem = LengthofSides / (2 * math.tan(math.pi/Numofsides))

print('The area of the polygon is:' + str(P*apothem*0.5))