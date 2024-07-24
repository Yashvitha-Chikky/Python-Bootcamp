a=24
if(a>=18 and a<24):
    print("only two wheelers")
elif(a>=24 and a<45):
    print("two and four wheeler")
else:
    print("all")



#print("enter num of apples")
#i=int(input())
#print("enter num of bananas")
#j=int(input())
#print("enter num of oranges")
#k=int(input())
#apples=15*i
#bananas=24*j
#oranges=5*k
#sum=0
#sum=apples+bananas+oranges
#if(sum<=700):
 #   print("he is not cheated")
#else:
 #   print("he is cheated")    


'''a=int(input())
if(a>0 and a%2==0):
    print("the number is positive and even")
elif(a<0 and a%2==0):
    print("the number is negative and even")
elif(a>0 and a%2!=0):
    print("the number is positive and odd")
else:
    print("the number is negative and odd")'''

#mrz is selected for olympics in the participating in the swimming competition only 1 winner is selected among the participants
# and how he got selected
#mrs
#mrx and mry are friends of z mrsx is participating in badminton,y in table tennis
#a/c to selection committee the reqirements for the badimtons players are(X)
#1.height=140cm
#2.weight=factors of 2
#3.bodyfat is less than 12%
#a/c to the selection committee requirements or table tenis are(Y)
#1.height=min 118cm to 148cm
#2.weight=factors of num of medals won by mrz
#3.bodyfat=14000
#a/c to the previous history z participated in 14 games out of which he is having success rate of 50% 
#write a program to check whether mrx,y,z from india travel in a same plane or not

x_height=int(input())
x_weight=int(input())
y_height=int(input())
y_weight=int(input())
if(x_height>=140 and x_weight==0):
    print("he got selected in badminton")
else:
    print("only y and z can travel")
    if(y_height>=118 and y_height<=148 and y_weight%7==0):
        print("he got selected in tennis") 
    else:
        print("all of them can travel")
        
