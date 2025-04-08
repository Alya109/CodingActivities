class Person:

    classvar1Company="PUP alumni corp."

    # def __init__(self, name, sex, profession):
    def __init__(self):
        # data members (instance variables)
        self.name = ""
        self.sex = ""
        self.profession = ""
        
    def populate(self, name1, sex1, profession1):
    # def __init__(self):
        # data members (instance variables)
        self.name = name1
        self.sex = sex1
        self.profession = profession1


    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)
    
    @classmethod
    def changeCompany(cls,newComp):
        cls.classvar1Company=newComp
        

# create object of a class

p200=Person()
p200.populate('jess','F','Engr')
p200.work()

# jessa = Person('Jessa', 'Female', 'Software Engineer')

# # call methods
# jessa.show()
# jessa.work()
# Person.changeCompany("new company")
# print(jessa.classvar1Company)

# p1=Person("JOhn","male","doctor")
# p100=Person("wick","male","killer")

# p100.show()
# p100.work()

# print(p100.classvar1Company)