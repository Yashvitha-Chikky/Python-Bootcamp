#write a code for single inheritence, multiple inheritance and multilevel
class Animal:
    def speak():
        return "animals are speaking"
class Dog(Animal):
    def bark():
        return "bow"
class Puppy(Dog):
    def puppy_speak():
        return "im puppy"
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj1.speak())
print(obj2.bark())
print(obj3.puppy_speak())