#produce a list of starting numbers from 1 million to 3
#iterate each value above, producing a list containing the iterative sequence
#check for and store highest sequence length for each above iteration

#number buckets
sequence = []
high_sequence_thus_far = []
high_starter_thus_far = []

#'hailstone sequence' helper function
def hailstone_sequencer(initial_value):
	if initial_value > 1:
		if initial_value % 2 == 0:
			sequence.append(initial_value/2)
			hailstone_sequencer(initial_value/2)
		else:
			sequence.append(3*initial_value+1)
			hailstone_sequencer(3*initial_value+1)
	return sequence

#main
initial_sequence_element = range(1000000,3,-1)
for starting_num in initial_sequence_element:
	if len(hailstone_sequencer(starting_num)) > len(high_sequence_thus_far):
		sequence = []
		high_sequence_thus_far = hailstone_sequencer(starting_num)
		high_starter_thus_far = starting_num

		print "high thus far: " + str(high_starter_thus_far) + " length: " + str(len(high_sequence_thus_far))
	
	sequence = []


print str(high_starter_thus_far)

	
