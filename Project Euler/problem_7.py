def is_a_prime(number):
	if number > 1:
		for x in range(2,number):
			if number % x == 0:
				return False
			else:
				continue
		return True
	else:
		False



import sys
i = 0
for x in xrange(sys.maxint):
	
	if is_a_prime(x):
		i += 1
		print str(x) + "prime index: " + str(i)
		if i>=10002:
			break
