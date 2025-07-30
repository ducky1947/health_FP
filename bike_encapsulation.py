class Bike:
    def __init__(self, brand, speed):
        self.__brand = brand
        self.__speed = speed

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        if brand:
            self.__brand = brand

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative")

    def display_info(self):
        print(f"Brand: {self.__brand}, Speed: {self.__speed} km/h")


bike1 = Bike("Yamaha", 60)
bike1.display_info()

bike1.__speed = 100  

bike1.set_speed(80)
bike1.display_info()

bike1.set_speed(-20)
