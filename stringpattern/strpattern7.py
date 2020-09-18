#write a program to print the characters present at even index and odd index seperately for the given string?
#s = durgasoft
#output = draot
 

s = input('enter some string to reverse: ')
i=0
print('characters present at even index: ')
while i<len(s):
	print(s[i])
	i=i+2

i=1	
print('characters present at odd index: ')
while i<len(s):
	print(s[i])
	i=i+2
	
#using slice operator
s = input('enter some string to reverse: ')
print('characters present at even index: ',s[0: :2])
print('characters present at odd index: ',s[1: :2])