# write a program to REVERSE content of the given string by using while loop?
#  str = mukesh
#  str = hsekum
 

s = input('enter some string to reverse: ')
output = ' '
i=len(s)-1
while i>=0:
	output=output+s[i]
	i=i-1
print(output)