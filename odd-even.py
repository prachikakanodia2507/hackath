# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
# Program to add two matrices using nested loop 

X = [[1,2,3], 
	[4 ,5,6], 
	[7 ,8,9]] 

Y = [[9,8,7], 
	[6,5,4], 
	[3,2,1]] 


result = [[0,0,0], 
		[0,0,0], 
		[0,0,0]] 

# iterate through rows 
for i in range(len(X)): 
# iterate through columns 
	for j in range(len(X[0])): 
		result[i][j] = X[i][j] + Y[i][j] 

for r in result: 
	print(r) 
