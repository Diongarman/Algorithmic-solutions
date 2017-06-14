def is_a_prime(candidate):
	#trial division
	for witness in range(2,int(candidate**0.5)+1):
		if candidate % witness == 0:
			return False
	return True

primes = []
for x in range(2,2000000):
	if is_a_prime(x):
		primes.append(x)


print sum(primes)