def digit_counter():
	def fibonacci_generator(n):
		F1 = 1
		F2 = 1
		N = F1+F2

		for x in range(n):
			F1 = F2
			F2 = N
			N = F1+F2
		return N

	counter = 0
	while (len(str(fibonacci_generator(counter))) < 1000):
		counter += 1
		#print 'index: ' + str(counter) + ' term: ' + str(fibonacci_generator(counter))
	return counter + 3

print digit_counter()