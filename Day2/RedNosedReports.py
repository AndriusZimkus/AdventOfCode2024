reports = []
with open('input.txt', 'r') as file:
	for line in file: # read rest of lines
		currentRow = []
		for x in line.strip().split():
			currentRow.append(int(x))
		reports.append(currentRow)


def isReportSafe(report):
	previousLevel = -1
	isIncreasing = False
	for i in range(len(report)):
		if i == 0:
			continue
		elif i == 1:
			isIncreasing = report[i] > report[i-1]
		
		diff = report[i] - report[i-1]
		if isIncreasing and report[i] <= report[i-1]:
			return False
		if not isIncreasing and report[i] >= report[i-1]:
			return False
		if abs(diff) > 3:
			return False
		
	return True

totalSafe = 0	
for report in reports:
	if isReportSafe(report):
		totalSafe +=1

print ("Undampened safe count:", totalSafe)

def isReportSafeDampened(report):

	for i in range(len(report)):
		currentReport = report[:i] + report[i+1:]
		if isReportSafe(currentReport):
			return True
	return False
	
totalSafeDampened = 0	
for report in reports:
	if isReportSafeDampened(report):
		totalSafeDampened +=1
		
print ("Dampened safe count:", totalSafeDampened)



		
		
		
