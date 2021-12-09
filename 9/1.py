with open('data.txt') as data_file:
    lines = [[int(char) for char in line] for line in  data_file.read().split('\n')]
lines = list(map(list, zip(*lines))) # Transpose

def check_adjacent(x, y):
	to_check = [10, 10, 10, 10]
	if x != 0:
		to_check[0] = lines[x-1][y]
	if y != 0:
		to_check[1] = lines[x][y-1]
	if x != len(lines)-1:
		to_check[2] = lines[x+1][y]
	if y != len(lines[x])-1:
		to_check[3] = lines[x][y+1]
	m = min(lines[x][y], min(to_check))
	if m == lines[x][y]:
		return (0, 0)
	return [(-1, 0), (1, 0), (0, -1), (0, 1)][to_check.index(m)]

mins = []
for x, column in enumerate(lines):
	for y, cell in enumerate(column):
		if check_adjacent(x, y) == (0, 0) and cell != 9:
			mins.append(cell)

print(sum([m+1 for m in mins]))