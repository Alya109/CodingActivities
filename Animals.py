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
    def make_sound(self):
        print("Roar!")
    def describe(self):
        print(f"{self.name} is a lion who lives in ....He is currently {self.age} years old!")
        
    def roar(self):
        print("Roars loudly.")

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")
    def describe(self):
        print(f"{self.name} is a bird who lives in ....He is currently {self.age} years old!")
        
    def fly(self):
        print("Flies high in the sky.")

class Reptile(Animal):
    def make_sound(self):
        print("Hiss!")
    def crawl(self):
        print("Crawls stealthily.")


lion = Lion("Lion", 14)
bird = Bird("Bird", 10)
reptile = Reptile("Reptile", 12)

lion.make_sound()
lion.roar()

bird.make_sound()
bird.fly()

reptile.make_sound()
reptile.crawl()
