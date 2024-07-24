
count=0
print("enter the value of n\n")
n=int(input())
for i in range(2,n//2):#1,n
    if(n%i==0):
        count+=1
if(count==0):#==1
    print("n is prime")
else:
    print("n is not prime")

num=0
digit=0
original_num=0
reverse_integer=0
sum_of_digits=0
print("enter the number")
original_num=num
while(num!=0):
    digit=num%10
    sum_of_digits=sum_of_digits+digit
    reverse_integer=sum_of_digits*10+sum_of_digits
    original_num=original_num+reverse_integer
    if(original_num=reverse_integer):
        print("the number is palindrome")
    else:
        print("the number is not palindrome")   


