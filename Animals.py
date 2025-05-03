# Earl Lumabi
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Meeeehhhhh")
    def describe(self):
        print("Prints a description of the animal including its name and age.")

class Lion(Animal):
    def roar(self):
        print("Roars loudly.")

class Bird(Animal):
    def fly(self):
        print("Flies high in the sky.")

class Reptile(Animal):
    
