#13. replace the elements in an array with average of max and min element of an array
li=list(map(int,input().split(" ")))
avg=0
maxi=li[0]
for i in range(len(li)):
    if(li[i]>maxi):
        maxi=li[i]

mini=li[0]
for i in range(len(li)):
    if(li[i]<mini):
        mini=li[i]
    
avg=(maxi+mini)//2
for i in range(len(li)):
    li[i]=avg
print(*li)
