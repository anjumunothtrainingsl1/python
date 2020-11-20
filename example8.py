import json
data ={
    "emp":{
        "empId":"1001",
        "empName":"sara",
        "salary":898
    }
}

with open("emp.json","w") as writeFilePtr:
    json.dump(data,writeFilePtr)
    jsonString=json.dumps(data)
    print(jsonString)
    jsonString1=json.dumps(data, indent=4)
    print(jsonString1)


