string = input()
count = 0
maxCount = 0
for i in range(len(string)):
	if string[i] == string[max(0,i-1)]:
		count += 1
	else:
		count = 1
	
	maxCount = max(count,maxCount)
print(maxCount)