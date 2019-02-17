def search(a,srch):
	for i in range(len(a)):
		if (a[i]==srch):
			return i
	return -1
a=[8,9,10,11,12]
srch=10
result=search(a,srch)
if (result==-1):
	print("number doesnot exist")
else:
	print("number exist at index",result)
