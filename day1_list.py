##my_list=[2,1,3,4]#static
#my_list.append(9999)
#my_list.insert(8000,99)
#print(len(my_list))
#my_list.pop(2)
#my_list_2=[5,6,7,8]
#new_list=my_list+my_list_2#concatenate the strings
#new_list=my_list.copy()
#new_list.pop()
#cnt=my_list.count(2)
#print(cnt)
#my_list.sort()
#print(*my_list)

#taking list(inputs) from the user
#my_list=list(map(str,input().split(" ")))
#my_list.append(4)
#print(*my_list)

list=list(map(int,input().split()))
print("1.append")
print("2.pop")
print("3.sort")
print("4.hello,length")
choice=int(input())
if(choice==1):
    list.append(2)
elif(choice==2):
    list.pop(1) 
elif(choice==3):
    list.sort() 
else:
    a=len(list)
    print(f"hello length is {a}")   
print(*list)