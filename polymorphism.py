#polymorphism  poly=> many , morph=>form
#encapsulation => capsule


class cow:
    def say_hello(self):
        print("moo")


class dog:
    def say_hello(self):
        print("ruff")


class cat:
    def say_hello(self):
        print("meow")   

Bingo = dog() 
Clarabell = cow()
Jamie = cat()       

Bingo.say_hello()
Clarabell.say_hello()
Jamie.say_hello()

class Parent:
    def __init__(self, name, childName):
        self.name = name
        self.__childName = childName  #private

        #getter method
    def get_name(self):
        print(self.__childName)    


parent1 = Parent("Lawal", "Mariam") 

print(parent1.childName)