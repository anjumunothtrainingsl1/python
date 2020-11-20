import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\anjum\OneDrive\Desktop\citi- python-nov\movies.xml")
root = tree.getroot()
print("Root Element Tag", root.tag)
print("Root Element Text", root.text)
print("Root Element Attrib", root.attrib)

for child in root:
    print(child.tag,child.attrib)

for element in root.iter():
    print(element.tag)

print ("Movies ")
print("*"*50)
for element in root.iter('movie'):
    print(element.attrib)

print ("Description ")
print("*"*50)
for element in root.iter('description'):
    print(element.text)

print ("Movies With Description")
print("*"*50)
for element in root.iter('movie'):
    print(element.attrib["title"],  end=" ")
    for child in element:
        if child.tag == "description":
            print(child.text)
    print()


print ("Movies in 1992 ")
print("*"*50)
for element in root.findall("./genre/decade/movie/[year='1992']"):
    print(element.attrib)

print ("Movies with multiple='yes'")
print("*"*50)
for element in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(element.text)

print ("Movies with multiple='yes'")
print("*"*50)
for element in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(element.attrib["title"])


