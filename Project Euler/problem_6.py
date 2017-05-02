

def difference(n):

	dif = sum(list(map(lambda x: x,range(1,n+1))))**2 - sum(list(map(lambda x: x**2,range(1,n+1))))
	return dif

print difference(100)