import csv
with open(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\student.csv","w") as csvWriteFilePtr:
    studWriter=csv.writer(csvWriteFilePtr, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
    studWriter.writerow([101,"Sara","A"])
    studWriter.writerow([102, "Lara", "B"])
    studWriter.writerow([103, "Tara", "C",["singing","dancing"], [10,20,25]])
    studWriter.writerows([[104,"King","A",None],[105,"Piyush","B"]])

projectArr=[{"projectId":"P101","projectName":"Store Front","projectDescription":"E Commerce Application"},
{"projectId":"P102","projectName":"CueBack","projectDescription":"Social Networking"}];

with open(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\project.csv","w") as csvWriteFilePtr:
    fieldNames=["projectId","projectName","projectDescription"]
    projectWriter=csv.DictWriter(csvWriteFilePtr,fieldnames=fieldNames,quoting=csv.QUOTE_NONNUMERIC,quotechar='"')
    projectWriter.writeheader()
    for item in projectArr:
        projectWriter.writerow(item)