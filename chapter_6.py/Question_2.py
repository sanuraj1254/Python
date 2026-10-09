marks1 = int(input("Enter the marks of first subject: "))
marks2 = int(input("Enter the marks of second subject: "))
marks3 = int(input("Enter the marks of third subject: "))

# Correct percentage calculation
percent = (marks1 + marks2 + marks3) * 100 / 300

# Checking passing condition
if percent >= 40 and marks1 > 33 and marks2 > 33 and marks3 > 33:
    print("You are passed:", percent)
else:
    print("Fail", percent)
