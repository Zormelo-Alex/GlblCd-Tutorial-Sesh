class Calculator:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        # if(self.num2 == 0):
        #     return "Invalid parameter reading second value \nValue can't be zero"
        return self.num1 / self.num2
    
