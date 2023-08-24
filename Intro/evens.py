def evens(x, y):
	while x <= y:
		if x % 2 == 0:
			print(x)
		x = x + 1
		


numOne = int(input("Please enter the first number\n"))
numTwo = int(input("Please enter the second number\n"))

evens(numOne, numTwo)

