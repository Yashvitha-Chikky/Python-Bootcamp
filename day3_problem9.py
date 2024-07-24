#9.find the  element present in k+n index 
#k is given by user        k=3,n=4
#k=3,':6,8,4,61,2            k=80 70 54 36 72
#n=1                      o/p=error
#0/p=2

'''li=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
a=len(li)
if(a < k+n):
    print("error")
else:
    for i in range(a-1):
        print(li[k+n])
        break

#10
#  print the element in a particular index 

li=list(map(int,input().split(" ")))
k=int(input())
if(k<len(li)):
    print(li[k])
else:
    a=k%len(li)
    print(li[a])

'''

my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])




