class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Owl(Bird):
    def sound(self):
        print("Owl hoots")

def make_sound(bird):
    bird.sound()

make_sound(Sparrow())
make_sound(Owl())
