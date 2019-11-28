x = 10
ac = 0
while x > 0:
	ac +=1
	print("")
	for i in range(x-1):
		print(" ",end="")
	for i in range(ac):
		print("#",end="")
	x-=1
