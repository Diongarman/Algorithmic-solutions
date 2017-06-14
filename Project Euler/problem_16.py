#What is the sum of the digits of the number 2^1000?

n = 2**1000
sum([int(d) for d in str(n)])