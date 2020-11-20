import csv

with open(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\rest.csv","r") as csvFilePtr:
    csvReader=csv.reader(csvFilePtr)
    lineCount=0
    for row in csvReader:
        if lineCount == 0:
            print("Column Names",row)
            print("Column names are :",(",".join(row)))
            colList=row
            lineCount+=1
        else:
            for i in range(len(colList)):
                print(colList[i] , " : " , row[i])
            print("*"*30)

with open(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\rest.csv","r") as csvFilePtr:
    csvReader=csv.DictReader(csvFilePtr)
    print(type(csvReader))
    lineCount=0
    for row in csvReader:
        if lineCount == 0:
            print("Column names are :", (",".join(row)))
            lineCount += 1
        else:
            print(row["city"])
