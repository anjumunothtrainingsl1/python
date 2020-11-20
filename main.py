import json
with open(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\zipcode1.json","r",encoding="utf-8") as readFilePtr:
    data=json.load(readFilePtr)
    #print(data)
    for i in range(len(data)):
        print("City",data[i]["city"])
        print("Latitude",data[i]["loc"][0])
        print("Longitude", data[i]["loc"][1])