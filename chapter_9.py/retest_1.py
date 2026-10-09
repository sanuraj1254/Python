f=open("poem.txt")
content = f.read()

if ("twinkle"in content):
    print(" the word twinkle is present in the file ")

else:
    print("the word twinkle is not present in the file")    
f.close()