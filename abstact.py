from abc import ABC,  abstractmethod

class Animal(ABC):
    #abstact method should implement in all subclasses
    @abstractmethod
    def move():
        pass

class Human(Animal):
    def    
