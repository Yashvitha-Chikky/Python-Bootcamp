'''n=int(input())
if(n%400==0):
    print("leap year")
else:
    print("not a leap year")'''
#print a leap year in a given range

a=int(input())
b=int(input())
for i in range(a,b+1):
    if a%400==0:
        print(a)