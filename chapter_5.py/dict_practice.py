marks = {
    "sanu" : 90,
    "piyush" : 80,
    "satyam" : 70
}

#print(marks.items())
#print(marks.keys())
print(marks.values())
marks.update({"sanu": 99})
print(marks)
print(marks.pop("satyam"))