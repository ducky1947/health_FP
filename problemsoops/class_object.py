class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

car1 = Car("Toyota", "Red")
car1.display()
