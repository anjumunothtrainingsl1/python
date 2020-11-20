class Employee:
    def __init__(self,p1,p2,p3):
        self.empId=p1
        self.empName=p2
        self.salary=p3

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if(value >0):
            self.__salary=value
        else:
            raise ValueError("Salary cannot be lower than zero ")



sara =Employee(101,"sara",89)
george=Employee(102,"george",12345)
#george.salary=-99
print("George salary",george.salary)
tara =Employee(103,"tara",99)

# static methods
# Classname.method()
# creating utility functions
# no need to create an instance


class Book:
    # class var
    ctr=0
    @staticmethod
    def myStaticFunction(name):
        names=name.split(" ")
        if(len(names) <=1):
            return False
        else:
            return True

    @staticmethod
    def incCounter(p1):
        ctr=ctr+p1

res=Book.myStaticFunction("Monk who sold his ferrari")
print("Res ",res)

#@classmethod
class Student:

    def __init__(self,fn,ln):
        self.firstName=fn
        self.lastName = ln

    def __str__(self):
        return "FirstName" + self.firstName+" Last Name"+self.lastName

    @classmethod
    def fromClubbedName(cls,name):
        fn,ln=map(str,name.split(" "))
        studObj=cls(fn,ln) # call the constructor
        return studObj

karan=Student("Karan","Goyal")
Lara=Student.fromClubbedName("Lara Dutta")
print("Karan",karan)
print("Lara",Lara);