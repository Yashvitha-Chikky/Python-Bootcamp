#prime number or not
'''n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("number is prime")
else:
    print("number is not prime")
    '''
a=int(input())
r=a**(1/2)
count=0
if a<2:
    print("number is not prime")
elif a==2:
    print("number is prime")
for i in range(2,int(r+1)):
    if a%i==0:
        count+=1
        
if(count==0):
    print("prime")
else:
    print("not prime")