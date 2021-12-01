with open('1-1/data.txt') as data_file:
	points = data_file.read().split('\n')


c = 0
for i in range(len(points)):
	if i == 0:
		continue
	if int(points[i]) > int(points[i-1]):
		c += 1

print(c)