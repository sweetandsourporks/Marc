# Activity No: 2
# Task: Get the Smallest Biggest and Middle Number
# Description: Program that outputs the smallest, biggest, and middle numbers from a given user input of three numbers. 
# Student Name: Granada, Marc Justin Lee G.
# Course / Year-Section: BSIT 1-1
# Date: October 15, 2024
# Subject : Computer Programming 1 - COMP 002
# Lecturer: Brian D. De Vivar

def main():
    pass
choice= input("Choose if you want smallest, middle, or biggest: ")
num1= int (input("Enter a number from 1-10: "))
num2= int (input("Enter a second number from 1-10: "))
num3= int (input("Enter a third number from 1-10: "))
if choice == "biggest":

    if num1 > num2 > num3:
        print(choice, "is", num1)
    elif num2 > num1 > num3:
        print(choice, "is", num2)
    elif num3 > num1 > num2:
        print(choice, "is", num3)
    elif num1 > num3 > num2:
        print(choice, "is", num1)
    elif num2 > num3 > num1:
        print(choice, "is", num2)
    elif num3 > num2 > num1:
        print(choice, "is", num3)

if choice == "smallest":
    if num1 < num2 < num3:
        print(choice, "is", num1)
    elif num2 < num1 < num3:
        print(choice, "is", num2)
    elif num3 < num1 < num2:
        print(choice, "is", num3)
    elif num1 < num3 < num2:
        print(choice, "is", num1)
    elif num2 < num3 < num1:
        print(choice, "is", num2)
    elif num3 < num2 < num1:
        print(choice, "is", num3)

if choice == "middle":
    if num1 < num2 < num3:
        print(choice, "is", num2)
    elif num3 < num2 < num1:
        print(choice, "is", num2)
    elif num2 < num1 < num3:
        print(choice, "is", num1)
    elif num3 < num1 < num2:
        print(choice, "is", num1)
    elif num1 < num3 < num2:
        print(choice, "is", num3)
    elif num2 < num3 < num1:
        print(choice, "is", num3)

print("Thank you,come again!")
print("This code ")
if __name__=='__main_':
        main()
