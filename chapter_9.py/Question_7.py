with open("log.txt")as f :
        lines = f.readlines()

lineno = 1
found_lines = []

for line in lines:
        if "python" in line:
                found_lines.append(lineno)
        lineno += 1

if found_lines:
        print("pythin is in line(s) :",found_lines)

else:
        print("python is not present")                        