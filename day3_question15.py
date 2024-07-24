#15.find the duplicates in an array(repeated elements)
li=list(map(int,input().split(" ")))
li1=[]
for i in li:
    if (i in li1):
        li1.append(i)
        li+=li1
print(li1)        