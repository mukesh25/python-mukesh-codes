# write a program to REVERSE order of words present in the given String?
#  input = Learning python is very easy
#  output = easy very is python Learning
 

s = input('enter some string to reverse: ')
l = s.split()	#['Learning','python','is','very','easy']
print(l)
l1 = l[::-1]	#['easy','very','is','python','Learning']
print(l1)
output=' '.join(l1)
print(output)	# easy very is python Learning