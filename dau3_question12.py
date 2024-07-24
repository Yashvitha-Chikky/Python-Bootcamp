#find the min element i a given list
li=list(map(int,input().split(" ")))
mini=li[0]
for i in range(len(li)):
    if(li[i]<mini):
        mini=li[i]
print(mini)       