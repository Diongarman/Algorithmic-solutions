def palindrome():
	#First for loop finds largest palindrome
	for x in range(999**2,100**2,-1):
		if is_a_palindrome(x):
			#second for loop finds a three-digit and  even divisor for the palindrome from the previous loop
			for y in range(1000, 111, -1):
				if (x%y==0 and len(str(x/y)) < 4):
					
					return "{} multiplied by {} gives the palindrome: {}".format(y,x/y,x)
					
def is_a_palindrome(num):
	if str(num)[::-1][:len(str(num))/2] == str(num)[:len(str(num))/2]:
		return True

print palindrome()