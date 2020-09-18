# write a program for the following requirement?
#  input = a4b3c2
# output = aaaabbbcc
 
s = input('enter some String where alphabete symbol should be followed  by digit: ')
output=''
for ch in s:
	if ch.isalpha():
		x=ch
	else:
		d=int(ch)
		output = output+x*d	
print(output)