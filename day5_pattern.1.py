#1.*****
#  *****
#  *****
#  *****
#  *****
'''
n=int(input())
for i in range(0,n):                #i=row.j=coloum
    for j in range(0,n):
        print("*",end=" ")
    print( )
  '''
n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()