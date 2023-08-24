def lists(thing):
	num_sum = 0
	for i in thing:
		if i % 2 == 0:
			num_sum += i 
	return num_sum
	
	
result = lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)
