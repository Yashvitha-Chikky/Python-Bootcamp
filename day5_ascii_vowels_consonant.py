'''print(ord('A'))
print(ord('A')+3)
print(ord('0'))
print(chr("<"))
'''
#check how many vowels are in a string
s=input()
vow=['a','e','i','o','u']
count=0
for i in s:
    if i in vow:
        count+=1
print(count)

#consonants count

s=input()
s1=s.lower()
abc="bcdfghjklmnpqrstvwxyz"
vow=['a','e','i','o','u']
count,c=0,0
for i in s1:
    if i in vow:
        count+=1
for i in s1:
    if i in abc:
        c+=1
print(count,c)
