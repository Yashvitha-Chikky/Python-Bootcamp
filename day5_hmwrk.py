#print upper triangular matrix
#print lower triangular matrix
#print rhombus
#print parallelogram
#***
#  ***
#     ***
#print number pyramid
'''
for i in range(5):
    for j in range(5):
        if(i<j):
            print(" ",end="")
        else:
            print("*",end=" ")
    print()
    

for i in range(5):
    for j in range(5):
        if(i<j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''

for i in range(3):
    for j in range(3):
        if(i>j and i<=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()