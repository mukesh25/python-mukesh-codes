#  n=4
# ---D--------------- i = 0==>(4-0-1)==>3
# --D C-------------- i = 1==>(4-0-2)==>2
# -D C B------------- i = 2==>(4-0-3)==>1
# D C B A------------ i = 3==>(4-0-4)==>0

# No. of spaces in every row:(n-i-1)
# No. of symbols in each row:(i+1)
# Which symbol: (64+n-j)

# with in row it is not fixed symbols keep on changing
# with in row if keep on changing symbol. compulsary, you have to go nested loop.

n= int(input('Enter n value: '))
for i in range(n):
	print(' '*(n-i-1),end='')
	for j in range(i+1):
		print(chr(64+n-j),end=' ')
		#print(chr(65+j),end=' ')
	print()
	