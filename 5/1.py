with open('data.txt') as data_file:
	data = data_file.read().split('\n')

board_width = 1000

data = [[[int(x) for x in pos.split(',')] for pos in line.split(' -> ')] for line in data]
grid = [0] * board_width**2
for start, end in data:
	if start[0] == end[0]:
		axis = 1
	elif start[1] == end[1]:
		axis = 0
	else:
		continue
	
	for i in range(min(start[axis], end[axis]), max(start[axis], end[axis])+1):
		if axis == 0:
			index = start[not axis]*board_width+i
		else:
			index = start[not axis]+board_width*i

		grid[index] += 1

over_2 = len([cell for cell in grid if cell > 1])

print(over_2)