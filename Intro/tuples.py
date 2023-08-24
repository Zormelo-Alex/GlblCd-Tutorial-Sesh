def partition(x):
    con = None
    if x % 2 == 0:
        tup = (x, con)
    else:
        tup = (con, x)
    return tup


def partition_list(l):
    evenArr = []
    oddArr = []
    for i in l:
        if(i % 2 == 0):
            ans = partition(i)
            evenArr.append(ans)
        else:
            ans = partition(i)
            oddArr.append(ans)
    finalAns = (evenArr, oddArr)
    return finalAns


# value = int(input("Please enter the integer value\n"))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = partition_list(list)

print(results)