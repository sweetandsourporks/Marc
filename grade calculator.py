grades = int(input("Enter Your Grades: "))

if grades >= 90 and grades <= 100:
    print("A")
elif grades >= 80 and grades <= 89:
    print("B")
elif grades >= 75 and grades <= 79:
    print("C")
else:
    print("Failed")
