# 1 2 3 *
# 1 2 * * * 
# 1 * * * * *
# * * * * * * *
# 1 * * * * * 
# 1 2 * * * 
# 1 2 3 *
 

n= int(input('Enter n value: '))
for i in range(n):
	print('- '*(n-i-1) + '* '*(2*(i+1)-1))
for i in range(n-1):
	print('- '*(i+1)+'* '*(2*(n-i)-3))