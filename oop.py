class Student:
    def __init__(self, name, hobby, grade):
        self.name = name
        self.hobby = hobby
        self.grade = grade

    def introduce(self):
        print("My name is ", self.name)

    def read(self):
        print(self.name, " is reading") 

    def __del__(self):
         print("The object has been deleted ")    


 
student3 = Student("Prosper", "playing games", 9)
student4 = Student("Haddiyat", "reading", 10)
student5 = Student("Zainab", "cooking", 8)
student6 = Student("Mariam", "racing", 10)

student6.introduce()
student6.read()