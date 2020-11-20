class Box:
    # class var, instance var
    # methods
    ctr=0 # class var
    def __init__(self,s1=0,s2=0):
        self.side1=s1
        self.side2=s2
        self.__area=0
    def printDetails(self):
        print("Side1:",self.side1)
        print("Side2:", self.side2)
    def incCounter(self):
        self.ctr=self.ctr+1
    def setArea(self):
        self.__area = self.side1 * self.side2
        return self.__area

rect1=Box(10,20) # A class object with the name Box will be created
rect1.printDetails() # Box.printDetails(rect1)
print("Counter value",Box.ctr)
Box.ctr=Box.ctr+1
print("Counter value",Box.ctr)
print("Counter value",rect1.ctr)
rect2=Box(99,99)
print("Counter value",rect2.ctr)

rect3=Box()
rect3.printDetails()

rect4=Box(s2=20,s1=10)
rect4.printDetails()
#print("Area in rect4",rect4.setArea())
print("Area in rect4",rect4.setArea())

#print("Area in rect4",Box.__area)

# encapsulation , abstraction, polymorphism, inheritance
# private, public

class Cuboid(Box):
    def __init__(self,s1,s2,s3):
        #super().__init__(self,s1,s2)
        Box.__init__(self,s1,s2)
        self.side3=s3
        self.__area=0
    def display(self):
        self.printDetails()
        print("Side 3",self.side3)
    def setArea(self):
        self.__area = self.side1 * self.side2 *self.side3
        return self.__area
    def __str__(self):
        str1="Side 1 :"+str(self.side1)+" Side 2 :"+str(self.side2)+" Side 3: "+str(self.side3)
        return str1

    def __add__(self, other):
        return Cuboid(self.side1+other.side1,self.side2+other.side2,self.side3+other.side3)

    def __sub__(self, other):
        return Cuboid(self.side1 - other.side1, self.side2 - other.side2, self.side3 - other.side3)


cuboidObj1=Cuboid(10,20,30)

cuboidObj2=Cuboid(40,50,60)
cuboidObj1.display()
print("Area of the cuboid:",cuboidObj1.setArea())

print("Cuboid",cuboidObj1)
cuboidObj3=cuboidObj1+cuboidObj2
print("Cuboid obj3",cuboidObj3)
cuboidObj4=cuboidObj1-cuboidObj2
print("Cuboid obj4",cuboidObj4)

#simple,multilevel, multiple, hybrid
# box ---> Cuboid
# Multilevel ; box---> Cuboid ---> Polygon
# Multiple Java, c# -- not allowed super()
# Father, Mother ---> child
# multiple inheritance

# overriding

# static functions

class Father:
    def __init__(self,p1):
        self.attr1=p1

class Mother:
    def __init__(self, p1):
        self.attr2 = p1
class Child(Father,Mother):
    def __init(self,p1,p2):
        Father.__init__(self,p1)
        Mother.__init__(self,p2)