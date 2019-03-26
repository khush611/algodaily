
def revereseArray(arr, n): 
	

	rev = n * [0] 
	for i in range(0, n): 
		rev[n - i - 1] = arr[i] 
			
	for i in range(0, n): 
		arr[i] = rev[i] 
		
if __name__ == "__main__": 
	arr = [1, 2, 3, 4, 5, 6] 
	n = len(arr) 
	print(*arr) 
	revereseArray(arr, n); 
	print("Reversed array is") 
	print(*arr) 
	
