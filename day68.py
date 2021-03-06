
def kadane(arr, start, finish, n): 
	

	Sum = 0
	maxSum = -999999999999
	i = None

	finish[0] = -1


	local_start = 0
	
	for i in range(n): 
		Sum += arr[i] 
		if Sum < 0: 
			Sum = 0
			local_start = i + 1
		elif Sum > maxSum: 
			maxSum = Sum
			start[0] = local_start 
			finish[0] = i 

	if finish[0] != -1: 
		return maxSum 

	
	maxSum = arr[0] 
	start[0] = finish[0] = 0

	# Find the maximum element in array 
	for i in range(1, n): 
		if arr[i] > maxSum: 
			maxSum = arr[i] 
			start[0] = finish[0] = i 
	return maxSum 

def findMaxSum(M): 
	global ROW, COL 
	
	# Variables to store the final output 
	maxSum, finalLeft = -999999999999, None
	finalRight, finalTop, finalBottom = None, None, None
	left, right, i = None, None, None
	
	temp = [None] * ROW 
	Sum = 0
	start = [0] 
	finish = [0] 

	# Set the left column 
	for left in range(COL): 
		
		# Initialize all elements of temp as 0 
		temp = [0] * ROW 

		# Set the right column for the left 
		# column set by outer loop 
		for right in range(left, COL): 
			
			# Calculate sum between current left 
			# and right for every row 'i' 
			for i in range(ROW): 
				temp[i] += M[i][right] 

			Sum = kadane(temp, start, finish, ROW) 

			
			if Sum > maxSum: 
				maxSum = Sum
				finalLeft = left 
				finalRight = right 
				finalTop = start[0] 
				finalBottom = finish[0] 

	 
	print("(Top, Left)", "(", finalTop, 
							finalLeft, ")") 
	print("(Bottom, Right)", "(", finalBottom, 
								finalRight, ")") 
	print("Max sum is:", maxSum) 


ROW = 4
COL = 5
M = [[1, 2, -1, -4, -20], 
	[-8, -3, 4, 2, 1], 
	[3, 8, 10, 1, 3], 
	[-4, -1, 1, 7, -6]] 

findMaxSum(M) 


