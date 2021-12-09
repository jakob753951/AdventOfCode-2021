from functools import reduce

with open('data.txt') as data_file:
    lines = [[int(char) for char in line] for line in  data_file.read().split('\n')]
lines = list(map(list, zip(*lines))) # Transpose

basins = []
seen_cells = set()


def fill_basin(x, y, basin = None):
	if basin is None:
		basin = set()

	if lines[x][y] == 9:
		return
	if (x, y) in seen_cells:
		return
	
	basin.add((x, y))
	seen_cells.add((x, y))

	to_fill = []
	
	if x != 0:
		to_fill.append((x-1, y))
	if y != 0:
		to_fill.append((x, y-1))
	if x != len(lines)-1:
		to_fill.append((x+1, y))
	if y != len(lines[x])-1:
		to_fill.append((x, y+1))

	[fill_basin(next_cell[0], next_cell[1], basin) for next_cell in to_fill]
	return basin



i = 0
for x, column in enumerate(lines):
	for y, cell in enumerate(column):
		if cell == 9:
			continue
		if (x, y) in seen_cells:
			continue
		basins.append(fill_basin(x, y))

three_biggest = sorted(basins, key = len, reverse=True)[:3]
lens = [len(basin) for basin in three_biggest]
result = reduce(lambda acc, x: acc * x, lens)
print(result)