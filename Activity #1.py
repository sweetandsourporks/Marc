# Activity No: 1
# Task: Create a Simple Calculator Program
# Description: This is a calculator that works by inputting the first 2 numbers then deciding what arithmetic operation will be done
# Student Name: Granada, Marc Justin Lee G.
# Course / Year-Section: BSIT 1-1
# Date: October 5, 2024
# Subject : Computer Programming 1 - COMP 002
# Lecturer: Brian D. De Vivar

def main():
	num1 = int(input("Enter first Number: "))
	num2 = int(input("Enter second Number: "))
	choice = input("Enter your choice: ['a', 's', 'm','d']: ")
	
	if choice == 'a':
		result, op = num1 + num2, "sum"
	elif choice == 's':
		result, op = num1 - num2, "difference"
	elif choice == 'm':
		result, op = num1 * num2, "product"
	elif choice == 'd':
		result, op = num1 / num2, "quotient"
	else:
		result, op = 0, "invalid choice"
		
	print(f"The {op} of {num1} and {num2} is {result}")
	print("comeback again")
	
if __name__ == '__main__':
	main()
