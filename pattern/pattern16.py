#---*
#--* *
#-*   *
#*     *

n= int(input('Enter n value: '))
for i in range(n):
	#print('  '*(n-i-1)+'* ',end='')
	print('  '*(n-i-1),end='')
	print('* ',end='')
	if i>=1:
		#print('  '*(2*i-1)+'* ',end='')
		print('  '*(2*i-1),end='')
		print('* ',end='')
	print()
	
#-------------simple way----------------	
n= int(input('Enter n value: '))
for i in range(n):
	print('  '*(n-i-1)+'* ',end='')
	if i>=1:
		print('  '*(2*i-1)+'* ',end='')
	print()