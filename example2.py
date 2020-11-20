def greatestOfTwoNumbers(a,b):
    """ Function to find the greatest of 2 numbers """
    if(a>b):
        print("a",a, "is the greatest")
    else:
        print("b :",b," is the greatest")

greatestOfTwoNumbers(1,4)

ctr=222
def incCounter():
    ctr=0
    print("Ctr before increment",ctr)
    ctr=ctr+1
    print("Ctr After increment", ctr)

incCounter()

def splice(list1,pos,delCount,insertValue=[]):
    endPos=pos+delCount
    print(list1)
    if(len(insertValue) >0):
        addList=[]
        addList.append(insertValue)
        list1[pos:endPos]=addList
    else:
        del list1[pos:endPos]
    print(list1)

list1=[10,20,30,40,50]
#splice(list1,2,2,55)#[10,20,55,50]
splice(list1,2,2)# [10,20,50]


def primeNumbers(start=3,end=100):
    for i in range(start,end):
        flag=False
        for j in range(2,int(i/2)+1):
            if(i%j == 0):
                flag=True
                break
        if(flag == False):
            print(i)

primeNumbers()
primeNumbers(20);# 20 to 100
#primeNumbers(3,50)
primeNumbers(end=50)# default value for start
# positional arg; keyword args
primeNumbers(end=50,start=20)
primeNumbers(20,end=50)
#primeNumbers(start=50,100)SyntaxError: positional argument follows keyword argument

