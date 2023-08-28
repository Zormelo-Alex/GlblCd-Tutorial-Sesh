class Car:
    def __init__(self, color, plate_number, brand, no_of_wheels):
        self.color = color
        self.plate_number = plate_number
        self.brand = brand
        self.no_of_wheels = no_of_wheels
    
    def print_no_of_wheels(self):
        print(self.no_of_wheels)

    def drive():
        print("The car is moving forward")

    def playMusic():
        print("The car is playing music")

MrAdolfCar = Car("ash", 32457, "Lexus", 4)

MrAdolfCar.print_no_of_wheels()
