def partition(x):
    con = "none"
    if x % 2 == 0:
        tup = (x, con)
    else:
        tup = (con, x)
    return tup


def partition_list():
    return "A"


value = int(input("Please enter the integer value\n"))
print(f"The result is {partition(value)}")