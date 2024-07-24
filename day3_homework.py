#1.find even or odd
#2.find greatest of three
#3.find the sum of all the elements in an array
#4.*find peak element in an array
#5.find max element in an array
#6.find second max element in an array
#7. reverse an array without using built in functions
#8.find the sum of squares of given number
#9.find sum of squares of even and odd digits
#10.check whether given number is palindrome or not using while loop
#11.wap to print 1st n fibanocci series

'''n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")
    

a=int(input())
b=int(input())
c=int(input())
if(a>b):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
    


arr=list(map(int,input().split(" ")))
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print(sum)



arr=list(map(int,input().split(" ")))
peak_=arr[0]
for i in range(len(arr)):
    if(arr[i]>peak_):
        peak=arr[i]
print(i)



arr=list(map(int,input().split(" ")))
maxi=arr[0]
for i in range(len(arr)):
    if(arr[i]>maxi):
        maxi=arr[i]
print(maxi)
'''

arr=list(map(int,input().split(" ")))
arr.sort()
#for i in range(len(arr)):
#    arr=arr[i-1]
print(*arr-2)

'''

arr=list(map(int,input().split(" ")))
abc=0
for i in range(len(arr)):
    abc-=i
print(abc)
'''


'''
n=int(input())
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**2
    n=n//10
print(sum)
'

n=int(input())
sum,sum1=0,0
while n>0:
    rem1=n%10
    if(rem1%2==0):
        sum=sum+rem1**2
    n=n//10
    rem2=n%10
    if(rem2%2!=0):
        sum1=sum1+rem2**2
    n=n//10
print(sum,sum1)
'''
'''
n=int(input())
sum=0
reverse_num=0
while(n>0):
    rem=n%10
    sum=sum+rem
    reverse_num=reverse_num*10+rem
    n=n//10
if(n==reverse_num):
    print("palimdrome")
else:
    print("not palindrome")


li=list(map(int,input().split(" ")))
s1,s2=0,0
for i in range(0,len(li)):
    s1=s1+li[i]
    s2=s2+s1
print(s2)'''