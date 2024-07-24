#LCM of two numbers
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
x=a*b
while b!=0:
    a,b=b,a%b
print(x//a)
