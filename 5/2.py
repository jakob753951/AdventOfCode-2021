with open('data.txt') as data_file:
	data = data_file.read().split('\n')

board_width = 1000

data = [[[int(x) for x in pos.split(',')] for pos in line.split(' -> ')] for line in data]
board = [0] * board_width**2
for start, end in data:
	length = abs(start[0]-end[0]) | abs(start[1]-end[1])

	if start[1]-end[1] == 0:  # Horizontal
		formula = lambda i: board_width * start[1] + (min(start[0], end[0])+i)

	elif start[0]-end[0] == 0:  # Vertical
		formula = lambda i: board_width * (min(start[1], end[1])+i) + start[0]

	elif start[0]-end[0] == start[1]-end[1]:  # Down-Diag
		formula = lambda i: board_width * (min(start[1], end[1])+i) + (min(start[0], end[0])+i)

	elif end[0]-start[0] == start[1]-end[1]:  # Up-Diag
		formula = lambda i: board_width * (max(start[1], end[1])-i) + (min(start[0], end[0])+i)
	
	else:
		continue

	for i in range(length+1):
		index = formula(i)
		board[index] += 1

over_2 = len([cell for cell in board if cell > 1])

print(over_2)
