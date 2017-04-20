#Find the sum of the digits in the number 100! (100 factorial)

number = int(input("please enter a non-negative integer:"))

product = 1

li = []

for i in range(number):
    product = product * (i+1)

product
    
for x in str(product):
    
    li.append(int(x))


li2 = sum(li)
    
print(li2)
