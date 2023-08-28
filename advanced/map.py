def square(x):
    return x*x

mylist = [1, 2, 5, 7, 9]

# values come in streams which can only be accessed once so this is my remedy to using them multiple times

res = map(square, mylist)
res = list(res)

print(res)

for i in res:
    print(i)