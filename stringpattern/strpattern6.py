#write a program to REVERSE internal content of every second word present in the given string?
#input = one two three four five six
#output = one owt three ruor five xis 

s = input('enter some string to reverse: ')
l = s.split( )
print(l)				#['one','two','three','four','five','six']
i=0
l1 = []
while i<len(l):
	if i%2==0:
		l1.append(l[i])
	else:
		l1.append(l[i][::-1])
	i=i+1
print(l1)				#['one','owt','three','ruor','five','xis']
output=' '.join(l1)
print(output)			#one owt three ruor five xis