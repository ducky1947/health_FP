class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog1 = Dog()
dog1.speak()
dog1.bark()
