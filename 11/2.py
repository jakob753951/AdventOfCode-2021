with open('data.txt') as data_file:
    grid = [int(char) for char in data_file.read().replace('\n', '')]

has_flashed = set()

def get_adjacent(index):
	offsets = []
	
	min_x = 0 if index % 10 == 0 else -1
	max_x = 1 if index % 10 == 9 else 2
	
	min_y = 0 if index // 10 == 0 else -1
	max_y = 1 if index // 10 == 9 else 2

	for x_offset in range(min_x, max_x):
		for y_offset in range(min_y, max_y):
			offsets.append(index + (y_offset * 10) + x_offset)

	return offsets

def check_flash(index):
	global grid
	if grid[index] > 9 and index not in has_flashed:
		has_flashed.add(index)
		adjacent = get_adjacent(index)
		for i in adjacent:
			grid[i] += 1
		flashes = 1
		for i in adjacent:
			flashes += check_flash(i)
		return flashes
	return 0

def step():
	global grid, has_flashed
	grid = [cell+1 for cell in grid]

	has_flashed.clear()

	flashes = 0
	for i, _ in enumerate(grid):
		flashes += check_flash(i)
	
	grid = [0 if cell > 9 else cell for cell in grid]
	return flashes

def print_grid():
	global grid

	for i in range(10):
		print(''.join(str(x) for x in grid[i*10:i*10+10]))

time = 1
while step() != 100:
	time += 1

print(time)