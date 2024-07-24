for i in range(32,128):
    print(chr(i),end=" ")


for i in range(48,58):
    print(chr(i),end=" ")


#to print sum of digits using ascii values
s=input()
sum=0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)


#write a code to print all the capital letters in agiven string
s=input()

for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        
        print(i,end=" ")
    

#remove all the brackets from the given algebraic expression
n=input()
for i in n:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
    
#input=ABC,4
#o/p=DEF
n=input()
n1=n.upper()
for i in n1:
    print(chr(ord(i)+4),end="")
        