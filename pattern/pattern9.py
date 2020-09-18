#    1
#   2 2
#  3 3 3
# 4 4 4 4

# No. of spaces in every row:(n-i-1)
# which symbol: (i+1)
# How many times: (i+1)

# with in each row same symbol are taken
# inside row symbol are not changing that's why nested loop is not required.

n= int(input('Enter n value: '))
for i in range(n):
	print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
	