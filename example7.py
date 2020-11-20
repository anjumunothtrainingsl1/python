with open("sample2.txt","w",encoding="utf-8") as fileptr:
    fileptr.write("I hope all of u are enjoying the training")
    fileptr.write("Is it informative")
    fileptr.writelines(["this is the second line\n","this is the third line"])