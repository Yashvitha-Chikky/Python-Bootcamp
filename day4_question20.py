# password verifier
#mr.X is trying to create a new password for his instagram account.these are the required conditions for creating a new password
#1.minimun length is 8 max length is 15
#2.only @ , / are allowed in a password
#3.no spaces are allowed
#4.only alpha numerics are allowed
# you are supposed to print weak if length is exact 8,medium length is between 8 to 12, strong if length is between 12 to 15

s1="@yash/181"
a=len(s1)
count=0
if(a<8):
    print("follow the conditions")
for i in s1:
    if (i =='@' or i=='/' )and i!=" ":
        count+=1
        break
if(count>1):
    print("follow the steps")
        

if(a==8):
    print("weak")
elif(a>8 or a<12):
    print("medium")
else:
    print("strong")