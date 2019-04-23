
def countWays(N) : 


	if (N == 1) : 
		
		return 4

	countB=1
	countS=1

	for i in range(2,N+1) : 
	
		prev_countB = countB 
		prev_countS = countS 

		countS = prev_countB + prev_countS 
		countB = prev_countS 
	

	result = countS + countB 

	return (result*result) 

if __name__ == "__main__": 

	N = 3
	print ("Count of ways for ", N 
		," sections is " ,countWays(N)) 
	

