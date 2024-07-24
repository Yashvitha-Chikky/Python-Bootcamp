#multilevel inheritence
class Animal:
    def speak():
        return "animals are speaking"
class Dog(Animal):
    def bark():
        return "bow"
class Puppy(Dog):
    def puppy_speak():
        return "im puppy"
class Animal1:
    def speak1():
        return "animals are speaking"
class Cat(Animal):
    def bark1():
        return "meow"
class Kitten(Cat):
    def kitten_speak1():
        return "im kitty"
class Animals(Animal,Animal1):
    def speaks():
        return " i have all the animal properties"
obj1=Animal
obj2=Dog
obj3=Puppy
obj4=Animal1
obj5=Cat
obj6=Kitten
obj7=Animals
print(obj1.speak())
print(obj2.bark())
print(obj3.puppy_speak())
print(obj4.speak1())
print(obj5.bark1())
print(obj6.kitten_speak1())
print(obj7.speaks())
