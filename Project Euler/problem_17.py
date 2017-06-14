place_values = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
100:"hundred", 200:"twohundred",300:"threehundred",400:"fourhundred",500:"fivehundred",600:"sixhundred",700:"sevenhundred",
800:"eighthundred",900:"ninehundred",1000:"onethousand"}


def letter_count_1_to_99(number):
	number_string = ''

	#check if in dict, if so return value
	if number in place_values.keys():
		number_string += place_values[number]
		return len(number_string)	
	#if not in dict create number spelling and return value
	for x in range(len(str(number))):
		if len(str(number)[x:]) == 2 and int(str(number)[1]) > 0:
			number_string += place_values[int(str(number)[x] + '0')]
			number_string += place_values[int(str(number)[1])]
	return len(number_string)

def letter_count_100_to_199(number):
	number_string = ''
	prefix = ""
	suffix_number = int(str(number)[1:])
	hundreds_place = 100

	#check if in dicr
	if number in place_values.keys():
		number_string += place_values[number]
		return len(number_string)		
	#create 100s place prefix
	prefix += place_values[int(str(number)[0])]
	prefix += place_values[hundreds_place] + "and"

	#check if tens suffix is in dict, append to 100s prefix and return
	if suffix_number in place_values.keys():
		number_string += prefix + place_values[suffix_number]
		return len(number_string)	
	
	#create tens suffix if not in dict,a ppend to 100s prefix and return
	for x in range(len(str(suffix_number))):
		if len(str(suffix_number)[x:]) == 2 and int(str(suffix_number)[1]) > 0:
			number_string += prefix +place_values[int(str(suffix_number)[x] + '0')] + place_values[int(str(suffix_number)[1])]
	return len(number_string)


counter = 0
for x in range(1,100):
	counter += letter_count_1_to_99(x)
for x in range(100,1001):
	counter += letter_count_100_to_199(x)

#+3 for the missing 'one' prefix for the number 100
print counter + 3

