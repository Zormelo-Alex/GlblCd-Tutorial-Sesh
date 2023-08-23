def calculate(operator, x, y):
	#print(operator)
	
	if type(operator) != str:
		return "error! \nenter a valid operator!"
		
		
	operator = operator.lower()
	
	if operator == "add":
		return x + y
	elif operator == "subtract":
		return x - y
	elif operator == "multiply":
		return x * y
	elif operator == "divide":
		return x / y
	else:
		return "error! \nenter a valid operator!"
	

valOne = int(input("Please enter the first value\n"))
valTwo = int(input("Please enter the second value\n"))
op = input("Please enter your operator\n")
	
result = calculate(op, valOne, valTwo)

print("The correct answer is", result)

