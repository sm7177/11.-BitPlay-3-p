def maxConsecutiveOnes(x):

	count = 0

	while (x!=0):
		x = (x & (x << 1))

		count=count+1
	
	return count
n=int(input("Enter a number:"))
print(maxConsecutiveOnes(n))


