# write a program for the following requirement?
#  input = a4k3b2
# output = aeknbd
 
s = input('enter some String: ')
output=''
for ch in s:
	if ch.isalpha():
		output=output+ch
		x=ch
	else:
		d=int(ch)
		newc=chr(ord(x)+d)
		output=output+newc
print(output)