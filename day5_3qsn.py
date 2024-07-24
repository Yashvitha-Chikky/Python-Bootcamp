#wap to print all the vowels followed by consonants
s=input()
s1=s.lower()
abc="bcdfghjklmnpqrstvwxyz"
vow=['a','e','i','o','u']                   #ans=0
for i in s1:
    if i in vow:
        print(i,end=" ")                #ans+=i
for i in s1:
    if i in abc:
        print(i,end=" ")                #ans+=i


                                        #print(ans)
