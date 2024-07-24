#i/p=hello---------world
# o/p=-----------helloworld
s=input()
s1=""
s2=""
for i in s:
    if(ord(i)==45):
        s1+=i
    if(ord(i)>=97 and ord(i)<=122):
        s2+=i
print(s1,s2,end="")


#method 2
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)