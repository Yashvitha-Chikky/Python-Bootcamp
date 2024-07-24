# string methods are 
# #is alpha,is digit, is alam(alpha numeric)
# is upper, is lower,covertin in lower casr ,into upper case,title case,swap case
'''
s1="  hello world   "
print(s1.upper())#converts to uppercase
print(s1.lower())#converts to lowercase
print(s1.capitalize())#removes capital letters
print(s1.title())#first letter starts with capital
print(s1.swapcase())#upper to lower or lower to upper
print(s1.strip())#removes spaces
print(s1.replace('a','z'))#replaces a with z
print(s1.split())#into list
print(s1.split('o'))# divides at that letter and removes it

'''

s1="Hello World 123"
print(s1.isalpha())#if space is there returns false else true
print(s1.isnumeric())#checks whether the given is having numeris values and returns false if there is space
print(s1.isalnum())#if input is having both numeric and alpha values prints true else false
print(s1.isascii())#like it is numeric and not allows like-42
print(s1.isupper())#checks uppercase and if there returns true else false
print(s1.islower())#checks lowercase and returns true if they are else false
print(s1.istitle())#
print(s1.isnumeric())#is the number
print(s1.isdigit())#are from 0 to 9