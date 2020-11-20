def singleton(cls):
    singleton.instance = None
    def innerFunc(*args,**kwargs):
        if not singleton.instance:
            singleton.instance = cls(*args,**kwargs)
        return singleton.instance
    return innerFunc


@singleton
class Box:
    def __init__(self,p1,p2):
        self.side1=p1
        self.side2=p2

    def __str__(self):
        return "Side 1 :" + str(self.side1) + " Side 2:"+ str(self.side2)

b1=Box(10,20)
b2=Box(100,200)
print("B1 ",b1)
print("B2 ",b2)
print("B1 's id",id(b1))
print("B2 's id",id(b2))

@singleton
class Emp:
    def __init__(self,p1,p2,p3):
        self.empId=p1
        self.empName = p2
        self.salary = p3
    def __str__(self):
        return str(self.empId)+self.empName+str(self.salary)

sara=Emp(101,"sara",7687)
george=Emp(102,"george",7989)
print(sara)
print(george)

def myDecorator(f1):
    ctr = 1
    print("Inside decorator", ctr)
    def innerFunc(msg):
        return "hello"+ f1(msg)
    return innerFunc


def myFunc(msg):
    return msg

func1=myDecorator(myFunc) # Inside decorator 1
res=func1("Citibank");
print("Res",res) # hello Citibank
res=func1("RPS");
print("Res",res) # hello RPS
