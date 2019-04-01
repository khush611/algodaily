
def countRec(n, sum) : 
	
 
	if (n == 0) : 
		return (sum == 0) 

	if (sum == 0) : 
		return 1

	
	ans = 0

	
	for i in range(0, 10) : 
		if (sum-i >= 0) : 
			ans = ans + countRec(n-1, sum-i) 

	return ans 
	
	

def finalCount(n, sum) : 
	
	
	ans = 0

	
	for i in range(1, 10) : 
		if (sum-i >= 0) : 
			ans = ans + countRec(n-1, sum-i) 

	return ans 



n = 2
sum = 5
print(finalCount(n, sum)) 



