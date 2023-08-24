def even():
    num = int(input("Enter 1st number: "))
    num2 = int(input("enter 2nd number: "))
    while num2 > num:
        num2 = num2 - 1
        if num2 % 2 == 0:
            print(num2)
        
        
even()
