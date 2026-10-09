p1 = "make a lot of money"
p2 = "buy now"
p3 = "suscribe this"
p4 = "click this"

message = input("Enter your comment :")
if ((p1 in message or (p2 in message) or (p3 in message) or (p4 in message))):
    print("this is a spam")

else:
    print("this comment is not spam")