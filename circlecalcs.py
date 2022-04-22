# calculate circumferences and areas of a circle with radiuses 1-10
import math
radiuses = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
pi = math.pi
circumferences = []
areas = []

class circleCalc():
    def Circumference(radius):
        return round(2 * pi * radius, 2)

    def Area(radius):
        return round(pi * radius ** 2, 2)

for i in range(len(radiuses)):
    circumferences.append(circleCalc.Circumference(radiuses[i]))
    areas.append(circleCalc.Area(radiuses[i]))

rI = input("Select a radius 1-10: ")
print("The circumference of a circle with a radius of " + str(rI) + " is: " + str(circumferences[int(rI) - 1]))
print("The area of a circle with a radius of " + str(rI) + " is: " + str(areas[int(rI) - 1]))
