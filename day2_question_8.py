#8. given an spaces seperated integer list find the average of elements present in the even index
#li=list(map(int,input().split(" ")))
#sum,avg,count=0,0,0
#for i in range(0,len(li)):
#    if(i%2==0):
#        sum+=li[i]
#        count+=1
#        avg=sum/count
#print(avg)


#1.write a program to find area of a circle
#2.wap to find perimeter of a circle
#3.wap to find area of a triangle
#4.wap to find perimeter of a triangle
#5.find a program to write find prime numbers by sqrt method

print("enter the radius of a circle")
r=int(input())
pi=3.14
area_of_circle=2*pi*r
print("area of a circle is",area_of_circle)