def is_a_prime(number):
	if number >= 1:
		for x in range(2,number):
			if number % x == 0:
				return False
			else:
				continue
		return True
	else:
		False
#print is_a_prime(1)
print is_a_prime(2)
print is_a_prime(3)
#print is_a_prime(7)
#print is_a_prime(139)
#print is_a_prime(9)
#print is_a_prime(16)
#print is_a_prime(18)
print is_a_prime(15485863)
print is_a_prime(15485864)
