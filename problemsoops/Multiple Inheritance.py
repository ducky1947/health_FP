class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def skills(self):
        print("Drawing")

c = Child()
c.skills()
