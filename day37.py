
def countSetBits(x) : 
	
	count = 0
	
	while (x) : 
		x = x & (x-1) 
		count = count + 1
	
	return count 
	

def isBleak(n) : 

	for x in range(1, n) : 
		
		if (x + countSetBits(x) == n) : 
			return False
			
	return True
	

if(isBleak(3)) : 
	print( "Yes") 
else : 
	print("No") 

if(isBleak(4)) : 
	print("Yes") 
else : 
	print( "No") 
	

