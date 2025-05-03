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
    def describe(self):
        print(f"{self.name} is a reptile who lives in ....He is currently {self.age} years old!")
        

lion = Lion("Emu", 14)
bird = Bird("Shizuku", 10)
reptile = Reptile("Tsukasa", 12)

lion.make_sound()
lion.roar()
lion.describe()

bird.make_sound()
bird.fly()
bird.describe()

reptile.make_sound()
reptile.crawl()
reptile.describe()
