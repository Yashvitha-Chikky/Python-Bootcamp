#print a leap year in a given range

a=int(input())
b=int(input())
for i in range(a,b+1):
    if (i%4==0 and i%100!=0):
        print(i)
        