print("Welcome to the training on python")
i = 10
i = "hello"
i = 5.7
a,b,c=10,20,30
print("A = ",a);#10

# int, long, float, complex

str1="good morning"
print(str1) #"good morning"
print(str1[0]) #"g"
print(str1[2:5])# (od )
print(str1[2:])#"od morning"
print(str1[:6])#"good m"
print(str1[:])#"good morning"

print(str1*2) # good morninggood morning

print(str1+ "Team")

#str1[1]="j"
print("String after modification",str1) #
str1="hello team"

print(str1.capitalize()) #

# isdigit() isalnum() isaplha() isspace() isnumeric()

#find index
#startswith() endswith()

list1=[10,20,30,40]
print("List :",list1)
print("First elemnt in the array i s",list1[0])

# list can have values which belongs to diff types
# list can have repetitive values
# lists are mutable

for i in range(len(list1)):
    print(list1[i],end =" ")
list1=[0,1,2,3,4,5,6,7,8,9]
print(list1[2:4])# 2 3
list1[2]=100
print(list1);
#list1[2:4]=77 # error
list1[2:4]=[77]
print(list1) # [0,1,77,4,5,6,7,8,9]

list1[2:4]=[55,66]
print(list1) # [0,1,55,66,5,6,7,8,9]

list1[2:4]=[22,33,44,77,88]
print(list1) # [0,1,22,33,44,77,88,5,6,7,8,9]

del list1[2];
print(list1)#[0,1,33,44...]

list1.append("hello")
list1.append(True)
list1.append(12.4)
print(list1)

print(list1.count(0)) #1
list2=[-55,-66]
list1.extend(list2)
print(list1)

list1.insert(4,-99)
print(list1)

list1.remove(-99)

list1.pop() # remove the last element

list1.pop(5)

#tuple ()
# ordered immutable ; similar to lists

tup1=();
tup2=(10,20,30,40,50)
tup3=(30,)

print("Tuple",tup2)
print(tup2[0])
print(tup2[2:4])
print(tup2[2:20])
#tup2[0]=-99

tup4=tup2+tup3
print(tup4)

 # dictionary
 # keys -- unique; immutable(numbers,string,tuples)
 #values- any data type; not unique
dict1={"empId":101,"empName":"SARA"}
dict1["salary"]=8090  # new field
print(dict1)
dict1["empId"]=102 # update existing field
print(dict1)
print(dict1["empId"])
#print(dict1["deptId"])

del dict1["empName"]
print("Emp details",dict1)

dict1.clear()
print("Emp details",dict1)

del dict1
#print("Emp details",dict1)

dict1={"empId":101,"empName":"SARA","salary":"8798","empName":"Virat"}
print(dict1);# virat

dict2=dict1.copy()
dict2["empId"]=999;
print("Dict1",dict1) # 101 Virat 8798
print("Dict2",dict2) # 999 Virat 8798

listOfKeys=dict1.keys()
listofValues=dict1.values()
listOfItems=dict1.items()
print("Keys:",listOfKeys)
print("values",listofValues)
print("Items",listOfItems)

for key in dict1.keys():
    #print(key, end=" ;")
    print(key ,":" ,dict1[key])

print("Emp name",dict1.get("empName"))

dict2={"deptId":"D1"}
dict1.update(dict2);
print(dict1)

print(dict1.popitem())
dict1.setdefault("deptId","d1")
print(dict1)
dict1.setdefault("empId",6666)
print(dict1)

dict4={"empId":101,"NULL":None}
print(dict4)

# set is similar to list ;
# set - no repetitive values
# unordered collection
# sets are mutables but the elements should be immutable
set1={10,20,30}
var1={}; # dict
set2=set()# empty set
set1.add(40)
print("Set1 ",set1)
set1.add(20)
print("Set1 ",set1)
set1={0,"hello",4.5,True}

print("Set1 ",set1)
#set1={0,"hello",4,5,True,[1,2,3]}

set1.update([10,20,30])
print("Set1 ",set1)

set1.update({55,66,77})
print("Set1 ",set1)

set1.update([-1,-2],{-3,-4})
print("Set1 ",set1)

set1.remove(-1)
set1.discard(-4)
print("Set1 ",set1)
set1.discard(101);#have no effect
#set1.remove(101);# error

print(set1.pop())# random element
print("Set1 ",set1)

#union intersection difference
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set1.union(set2);


# tuples,lists and sets, frozen set(immutable set)
fs1=frozenset([1,2,3,4,5,1]);
print(fs1)

fs2=frozenset([3,4,5,6,7]);
print(fs1.union(fs2))

fs3=frozenset([1,2]);
print(fs3.issubset(fs1))











