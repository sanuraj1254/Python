"""f = open("sanu")

lines= f.readlines()

print(lines , type(lines))"""
f = open("sanu")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()    