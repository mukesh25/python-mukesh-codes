#Assume input string contains only alphabet symblols and diits.
#write a program to sort characters of the string, first alphabet symblols followed by digits?
#  input = 'B4A1D3'
# output = 'ABD134'
 

s = input('enter some alphanumeric String to sort: ')
alphabets = []
digits = []
for ch in s:
	if ch.isalpha():
		alphabets.append(ch)
	else:
		digits.append(ch)
#print(alphabets)
#print(digits)
output = ''.join(sorted(alphabets)+sorted(digits))
print(output)