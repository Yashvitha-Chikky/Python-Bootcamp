#multiple inheritence
class Father:
    def speak():
        return "father class"
class Mother:
    def speak1():
        return "mother class"
class Kid(Father,Mother):
    def speak2():
        return "iam kid i have the properties from father and mother class"
obj1=Father
obj2=Mother
obj3=Kid
print(obj1.speak())
print(obj2.speak1())
print(obj3.speak2())