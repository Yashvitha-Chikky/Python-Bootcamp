#11.find the maximum element in a given list
#test case:0
#12 23 36 44 45 57
#o/p=57
#test case:1
#56 78 -8 12 34 -99
#o/p=78

li=list(map(int,input().split(" ")))
maxi=li[0]
for i in range(len(li)):
    if(li[i]>maxi):
        maxi=li[i]
print(maxi)