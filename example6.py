# open, (read/write) , close
# modes -- r , w (create, truncate), x(exclusive creation -- file exists --fail), a , t(text),b(binary), + (r+b)
# encoding - utf-8
try:
    f=open("sample1.txt","r",encoding="utf-8")
    res=f.read(4)
    print(res)
    res = f.read(4)
    print(res)
    res = f.read(4)
    print(res)
    f.seek(0) # go back to 0th position
    print("Reading the entire lline")
    for line in f:
        print(line)
    f.seek(0);
    res=f.read()
    print("res",res)
    f.seek(0)
    print(f.readline())
    print(f.readline())
    f.seek(0)
    print(f.readlines())

except NameError:
    print("Name Error")
except:
    print("Error reading the file")
finally:
    f.close()
