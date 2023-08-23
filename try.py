def rlist(x, y):
	new_list = []
	while x <= y:
		if x % 2 == 0:
			new_list.append(x)
		x += 1
	return new_list

num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))

results = rlist(num1, num2)
print(results)
