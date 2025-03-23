# object => an instance of a class 
# OOP(Object Oriented Programming) => classes and objects
#class => a blueprint of an object
# constructor
#self => refers to the object itself

student1 = {
    "name": "mariam",
    "age": "13",
    "email": "mariam@mariam.com"
} 

class Students:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

student2 = Students("James", 19, "james@james.com")
student3 = Students("Favor", 16, "favor@favor.com")       
student4 = Students("Britney", 14, "britney@britney.com" )

print(student2.email)
print(student4.age)



class animal:
    def __init__(self,type,lifespan,botanicalname):
        self.type = type
        self.lifespan = lifespan
        self.botanicalname = botanicalname

animal1 = animal("dog", 12, "Canis lupus familiaris")
animal2 = animal("koala", 15, "Phascolarctos cinereus")    
animal3 = animal("beer", 30,"Ursidae")



print(animal2.lifespan)
print(animal3.type)
print(animal2.botanicalname)
