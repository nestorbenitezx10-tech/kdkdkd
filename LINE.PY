import math
# from MyPoint import MyPoint
# import MyPoint


class MyPoint:
    # constructor
    def __init__(self,x, y):
        # attributes/properties
        self.xCoor = x
        self.yCoor = y
    
    # behavior
    def moveUp(self):
        self.yCoor = self.yCoor + 1
    
    def moveDown(self):
        self.yCoor = self.yCoor - 1

    def moveRight(self):
        self.xCoor = self.xCoor + 1
    
    def moveLeft(self):
        self.xCoor = self.xCoor - 1
    
    def movePoint(self, newX, newY):
        self.xCoor = newX
        self.yCoor = newY
    
    def __str__(self): #(x,y)
        return f"({self.xCoor},{self.yCoor})"
    


# Line -> consist of two (2) points


# Implementation without composition
class Line:
    # constructor
    def __init__(self, x1, y1, x2, y2):
        # data fields the line object
        self.startPointX = x1
        self.startPointY = y1
        self.endPointX = x2
        self.endPointY = y2
    
    # methods
    # def changeStartX(self, newX):
    #     self.startPointX = newX
    
    # apply to all data field

    # distance formula
    def getLength(self):
        return math.sqrt(math.pow(self.startPointX - self.endPointX,2) + math.pow(self.startPointY - self.endPointY,2))

    def __str__(self):
        return f"The line starts at point ({self.startPointX},{self.startPointY}) and ends at point ({self.endPointX},{self.endPointY}) with a length of {self.getLength()}"

# line1 = Line(2,2,-2,-2)
# print(line1)
# line2 = Line(0,0,5,0)
# print(line2)

# line1.startPointX = 1
# line1.startPointY = 0
# print(line1)

# line2 = Line(0,0,3,5)
# print(line2)
# line2.endPointX = 10
# line2.endPointY = 8
# print(line2)

# composition
# A line is composed of two (2) point objects

class LineComposedOfPointsV1:
    # constructor
    def __init__(self, x1, y1, x2, y2):
        self.startPoint = MyPoint(x1, y1)
        self.endPoint = MyPoint(x2, y2)

    def getLength(self):
        return math.sqrt(math.pow(self.startPoint.xCoor - self.endPoint.xCoor,2) + \
                         math.pow(self.startPoint.yCoor - self.endPoint.yCoor,2))

    def __str__(self):
        return f"V1 -> Line starts at {self.startPoint} and ends at {self.endPoint} with a length of {self.getLength()}"

# line1 = LineComposedOfPointsV1(0,0,5,0)
# print(line1)
# # display endpoint x-coordinate
# print(line1.endPoint.xCoor)
# change the coordinates
# line1.startPoint.xCoor = 3
# line1.startPoint.yCoor = 2
# print(line1)

# startTemp = line1.startPoint
# startTemp.movePoint(1,1)

# print(line1)

# using movePoint method defined in the MyPoint class
# line1.startPoint.movePoint(3,2)
# line1.endPoint.movePoint(7,8)
# print(line1)

# instantiate/create a new Point object
# line1.startPoint = MyPoint(3,2)
# print(line1)

# # display startpoint y-coordinate
# print(line1.startPoint.yCoor)
# print(line1)

class LineComposedOfPointsV2:
    # constructor
    def __init__(self, sp:MyPoint, ep:MyPoint): # assume that the parameters are MyPoint objects
        self.startPoint = sp
        self.endPoint = ep
    
    def getLength(self):
        return math.sqrt(math.pow(self.startPoint.xCoor - self.endPoint.xCoor,2) + \
                         math.pow(self.startPoint.yCoor - self.endPoint.yCoor,2))

    def __str__(self):
        return f"V2 -> Line starts at {self.startPoint} and ends at {self.endPoint} with a length of {self.getLength()}"


# p1 = MyPoint(0,0)
# p2 = MyPoint(5,0)

# lineV2 = LineComposedOfPointsV2(p1, p2)
# print(lineV2)

# p1.xCoor = 3
 
# print(lineV2)

# linev2 = LineComposedOfPointsV2(MyPoint(0,0), MyPoint(5,0))
# print(linev2)
# linev2.startPoint.movePoint(3,2)
# # linev2.startPoint.movePoint(-1,3)
# linev2.startPoint.xCoor = -1
# linev2.startPoint.yCoor = 3
# print(linev2)

# lineV1 = LineComposedOfPointsV1(-1,0,2,5)
# print(lineV1)


# l1.startPoint.xCoor = 0
# l1.startPoint.yCoor = 1
# l1.endPoint.xCoor = 3
# l1.endPoint.yCoor = 4
# print(l1)
# print(l1.startPoint)
# print(l1.endPoint)


# A triangle is composed of 3 points
class Triangle:
    # constructor version 1
    def __init__(self, p1x, p1y, p2x, p2y, p3x, p3y):
        self.vertex1 = MyPoint(p1x, p1y)
        self.vertex2 = MyPoint(p2x, p2y)
        self.vertex3 = MyPoint(p3x, p3y)

    # constructor version 2 accepts point objects as arguments
    # def __init__(self, p1, p2, p3):
    #     self.vertex1 = p1
    #     self.vertex2 = p2
    #     self.vertex3 = p3

    # length of the sides
    # calculate length of side A
    def getLengthSideA(self):
        return math.sqrt(math.pow(self.vertex1.xCoor - self.vertex2.xCoor, 2) + math.pow(self.vertex1.yCoor - self.vertex2.yCoor,2))

    # calculate length of side B
    def getLengthSideB(self):
        return math.sqrt(math.pow(self.vertex2.xCoor - self.vertex3.xCoor, 2) + math.pow(self.vertex2.yCoor - self.vertex3.yCoor,2))

    # calculate length of side C
    def getLengthSideC(self):
        return math.sqrt(math.pow(self.vertex3.xCoor - self.vertex1.xCoor, 2) + math.pow(self.vertex3.yCoor - self.vertex1.yCoor,2))
    
    # perimeter
    def getPerimeter(self):
        perimeter = self.getLengthSideA() + self.getLengthSideB() + self.getLengthSideC()
        return perimeter 

    # area
    def getArea(self):
        semiP = self.getPerimeter() / 2
        area = math.sqrt(semiP * (semiP - self.getLengthSideA()) * (semiP - self.getLengthSideB()) * (semiP - self.getLengthSideC()))
        return area
    
    def __str__(self):
        return f"Length of the Sides: \nA = {self.getLengthSideA()}\nB = {self.getLengthSideB()}\nC = {self.getLengthSideC()}\nPerimeter = {self.getPerimeter()}\nArea = {self.getArea()}"
        
# tri1 = Triangle(0,0,4,5,3,2)
# print(tri1)
# print(tri1.getLengthSideA())
# print(tri1.getLengthSideB())
# print(tri1.getLengthSideC())
# print(tri1.getArea())
# print(tri1.getPerimeter())

# tri2 = Triangle(0,0,1,1,2,1)
# print(tri2.getLengthSideA())
# print(tri2.getLengthSideB())
# print(tri2.getLengthSideC())
# print(tri2.getArea())
# print(tri2.getPerimeter())
# print(tri2)

# for version 2 constructor
# tri1 = Triangle(MyPoint(0,0),MyPoint(4,5),MyPoint(3,2))
# print(tri1)

# v1 = MyPoint(0,0)
# v2 = MyPoint(4,5)
# v3 = MyPoint(3,2)

# tri2 = Triangle(v1, v2, v3)
# print(tri2)


# CIRCLE

class Circle:
    # v1
    def __init__(self, x, y, r):
        self.center = MyPoint(x,y)
        self.radius  = r

    # v2
    # def __init__(self, centerpoint, rad):
    #     self.center = centerpoint
    #     self.radius = rad

    # methods
    # diameter, area, circumference
    def getDiameter(self):
        return self.radius * 2
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        # return math.pi * self.radius * self.radius
        return math.pi * math.pow(self.radius,2)
    
    def __str__(self):
        return f"Circle with radius {self.radius} has an area of {self.getArea()} and a circumference of {self.getCircumference()}"

c1 = Circle(0,0,5)
print(c1)
# c2 = Circle(3,-1,7.5)
# print(c2)

# square, rectangle, etc.

# SQUARE
# side

# reading assignment
# DATA FIELD ENCAPSULATION


