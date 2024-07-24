#how to reverse a number***important****
n=121
rev=" "
a=n
while n>0:
    rem=n%10
    rev=rev+str(rem)
    n=n//10

if(a==int(rev)):
    print("the number is palindrome")
else:
    print("the number is not a palindrome")


