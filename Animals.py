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
        
    def roar(self):
        print("Roars loudly.")

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")
        
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
