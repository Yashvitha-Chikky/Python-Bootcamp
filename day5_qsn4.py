#print the non repeating characters (unique characters )in a string
'''
s=input()
s1=s.lower()
ans=""
for i in s1:
    if i not in ans:
        ans+=i
print(ans)

#hello123world
#0/p=6
s=input()
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)



s="hello123world"
s1="0123456789"
sum=0
for i in s:
    if i in s1:
        sum+=int(i)
print(sum)

'''

#reverse the numbers present in a given string
s="hello 1234 world"
s1="0123456789"
ans=""
for i in s:
    if i in s1:
        ans+=i
        
s2=int(ans)
s3=""

while(s2>0):
    rem=s2%10
    s3=s3+str(rem)
    s2=s2//10
print(int(s3))