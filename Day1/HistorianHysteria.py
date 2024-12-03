#Read input

firsts = []
seconds = []
with open('input.txt', 'r') as file:
	for line in file: # read rest of lines
		currentRow = []
		xs = line.strip().split();
		firsts.append(int(xs[0]))
		seconds.append(int(xs[1]))
		
		#for x in line.strip().split():
		#	currentRow.append(int(x))



totalDistance = 0
firsts.sort()
seconds.sort()

for i in range (len(firsts)):
	currentDiff = abs(firsts[i] - seconds[i])
	totalDistance += currentDiff
	
# for row in rows:
	# print(row)
	# currentDiff = abs(row[1]-row[0])
	# totalDistance += currentDiff

print ("Total distance:", totalDistance)

similarityScore = 0
for x in firsts:
	countInSeconds = seconds.count(x)
	similarityScore += x * countInSeconds
	
print ("Similarity score:", similarityScore)