

input = open('input.txt', 'r').readlines() #take input, open as input

with open('output.txt', 'w') as file: #open an output file, create as output
	for i in range(len(input)):
		for j in range(len(input)):
			if input[i] != input[j]: #if input i and input j are not an identical match, add them to the beginning of the password
				file.write('Phrase1'+'Phrase2' + input[i].strip() + input[j].strip() + '\n')