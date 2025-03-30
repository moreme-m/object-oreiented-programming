# inheritance  ==> concept of using a parents class aattributes and methods
# super refers to the parent

class Granddad:
    def __init__(self, aggresive, eyes):
        self.aggresive = aggresive
        self.eyes = eyes
    def introduce(self):
        print("My eye color is ", self.eyes)

class Daughter(Granddad):
    def __init__(self, name, age, eyes, aggresive):
        self.name = name
        self.age = age
        super().__init__(aggresive,eyes)

granddad1 = Granddad(True, "black")
daughter1 = Daughter("Mercy", 20 , "blue", False)
daughter1.introduce()        


