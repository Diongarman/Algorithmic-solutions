import sys

#input the value that you want the largest prime factor of into command line arguments for this script

#helper function
def is_a_prime(number):
	if number > 1:
		for x in range(2,int(number**(0.5)+1)):
			if number % x == 0:
				return False
			else:
				continue
		return True
	else:
		False

def get_primes(number):
	prime_factors = []
	for num in range(2,int(number**(0.5)+1)):
		if is_a_prime(num) and number%num==0:
			prime_factors.append(num)
	if len(prime_factors)==0:
		return str(sys.argv[1]) + " is already prime, hence has no other factors"
	return "the prime factors of "+ sys.argv[1] + " are: " + str(prime_factors) + " of which the largest is " + str(max(prime_factors))

print get_primes(int(sys.argv[1]))

"""

###### Flow Tables ########

e.g. is_a_prime(5)

x in range(2, 3)

x	5%2==0 action
2	F		ctn
			break for loop
			return True



e.g is_a_prime(16)

x in range(2, 5)
x	16%2==0 action
2	F		ctn
3	T		return False


e.g is_a_prime(17)

x in range(2, 5)

x	17%2==0 action
2	F		ctn
3	F		ctn
4	F		ctn
			break for loop
			return True

"""



""" 
e.g. get_primes(17)

for num in rannge(2,5)

n    is_a_prime(n)    number%n==0    action
2    T                F              ctn
3    T                F              ctn
4    F                F              ctn
									 break
									 return statement 


"""
