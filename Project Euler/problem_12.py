import sys

def _factors(num):
	number_of_factors = 0
	for x in range(1,int((num)**0.5)):
		if num%x == 0:
			number_of_factors += 2
		else:
			continue

	return number_of_factors

def sequence_of_partial_sums():
	for i in xrange(sys.maxint):
		yield (i*(i+1))/2

def evaluator():
	for next_tri in sequence_of_partial_sums():
		print next_tri, _factors(next_tri)
		if _factors(next_tri) < 500:
			continue
		else:
			print 'First triangle number with over 500 factors is: ' + str(next_tri)
			break
evaluator()

