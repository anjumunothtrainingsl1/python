#lambda function
# anonymous function
# one line function
# pass function as a param to another function

f1=lambda x:x*x
print("10 square is", f1(10))

# map(func, iterable)
list1=[1,2,3,4,5]
def square(x):
    return x*x
squareList1=list(map(square, list1))
print("square list1",squareList1)

squareList2=list(map(lambda x:x*x,list1))
print("square list2",squareList2)

list2=[{"empId":101,"empName":"Sara"},
       {"empId":102,"empName":"Sana"},
       {"empId":103,"empName":"Tara"},
       {"empId":104,"empName":"Lara"}]
def myFunc1(emp):
    return emp["empId"]

empIdList=list(map(myFunc1,list2))
print("Empl Id",empIdList)

def filterFunction(emp):
    if(emp["empName"].startswith("S")):
        return True



empWithNameStartingWithS=list(filter(filterFunction,list2))
print("Emp",empWithNameStartingWithS)


#closure functions
# function returning a function

def outerFunc(msg):
    def innerfunc():
        print(msg)
        return msg
    return innerfunc

f1=outerFunc("good morning")
res=f1()
print("Result :",res);# good morning; error

# decorators
def outerWrapper(func):
    def innerFunc(msg):
        res="Hello"+func(msg)
        return res
    return innerFunc

def upperDecorator(func):
    def innerFunc(msg):
        res=func(msg).upper()
        return res
    return innerFunc

@upperDecorator
@outerWrapper
def sayHello(msg):
    return msg;

# upperDecorator(outerDecorator(sayHello(" Citibank")))
#f2=outerWrapper(sayHello)
#res=f2(" Citi")
#print("Res",res) # Hello City

res=sayHello(" Citibank")
print("Result = ",res)

def divideDecorator(func):
    def innerfunc(p1,p2):
        if(p2 == 0):
            return "Denominator cannot be zero"
        else:
            return func(p1,p2)
    return innerfunc


@divideDecorator
def divideTwoNumbers(a,b):
    return a/b

f1=divideDecorator(divideTwoNumbers);
res=f1(10,2);

res=divideTwoNumbers(10,2) # diviseDecorator(divideTwoNUmbers)
print("Res=",res)
res=divideTwoNumbers(10,0)
print("Res=",res)

def myDecorator(func):
    def innerFunc(*args,**kwargs):
        print("Positional args",args)
        print("Keyword args",kwargs)
        for k in kwargs.keys():
            print("Key word args are",k)
            kwargs[k]=-99
        return func(*args,**kwargs)

    return innerFunc


@myDecorator
def myFunc4(p1=1,p2=2,p3=3,p4=4):
    return p1+p2+p3+p4

res=myFunc4(10,20,30,40)
print("Res=",res)

res=myFunc4(10,20,p4=30,p3=40)
print("Res=",res)
