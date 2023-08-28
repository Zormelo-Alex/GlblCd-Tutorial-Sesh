from functools import reduce

def sumOfNums(x, y):
    return x+y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# values come in streams which can only be accessed once
res = reduce(sumOfNums, numbers)

print(res)
