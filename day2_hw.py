#1.write a program to find area of a circle
#2.wap to find perimeter of a circle
#3.wap to find area of a triangle
#4.wap to find perimeter of a triangle
#5.find a program to write find prime numbers by sqrt method


print("enter the radius of a circle")
r=int(input())
pi=3.14
area_of_circle=2*pi*r
print("area of a circle is",area_of_circle)

print("enter the radius")
r=int(input())
pi=3.14
perimeter_of_circle=pi*r**2
print("perimeter of a circle is",perimeter_of_circle)

print("enter the base")
b=int(input())
print("enter the height")
h=int(input())
area_of_triangle=(1/2)*b*h

print("area of triangle is",area_of_triangle)
a=int(input())
b=int(input())
c=int(input())
perimeter_of_triangle=a+b+c
print("perimeter of triangle is",perimeter_of_triangle)
