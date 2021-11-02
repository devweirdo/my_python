f = "fizz"
b = "buzz"

for i in range(1,101):
	if (i%2 == 0 and i%5 == 0):
		print("{} this is {}{}".format(i,f,b))
	elif i%2 == 0:
		print("{} this is {}".format(i,f))	
	elif i%5 == 0:
		print("{} this is {}".format(i,b))
