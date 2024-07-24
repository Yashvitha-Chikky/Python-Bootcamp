#creation of class
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    
#creation of instance of a class
obj1=Myclass
obj2=Myclass
obj3=Myclass
obj4=Myclass
obj5=Myclass

print(obj1.add(2,5))
print(obj2.sub(12,5))
print(obj3.div(30,12))
print(obj3.mul(2,8))
print(obj3.mod(5,10))


#declaring of constructor
#def_init(self)