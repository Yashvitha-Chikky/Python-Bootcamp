#14.find the missing number in an array .sequence of array will be given
li=list(map(int,input().split(" ")))
n=int(input())
sum=0
a=n*(n+1)//2
for i in li:
    sum+=i
print(a-sum)


