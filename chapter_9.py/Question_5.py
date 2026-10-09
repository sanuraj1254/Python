with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Python is persent")

else:
    print("python is not present")
