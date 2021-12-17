import functools

with open('data.txt') as data_file:
	grid = [[int(char) for char in line] for line in data_file.read().split('\n')]
grid = list(map(list, zip(*grid))) # Transpose


def is_inbounds(grid: list[list[int]], coord: tuple[int, int]):
	return ((0 <= coord[0] < len(grid)) and (0 <= coord[1] < len(grid[0])))

@functools.cache
def cost(coord: tuple[int, int], visited: tuple[tuple[int, int]]):
	this_value = grid[coord[0]][coord[1]]

	if coord[0] == len(grid)-1 and coord[1] == len(grid[0])-1:
		return this_value

	directions = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1),
	]

	costs = []
	for direction in directions:
		dir_coord = (direction[0] + coord[0], direction[1] + coord[1])
		if not is_inbounds(grid, dir_coord):
			continue
		if dir_coord in visited:
			continue
		costs.append([cost(dir_coord, (*visited, dir_coord)), dir_coord])
	if len(costs) == 0: 
		return 99999999
	min_cost = min(costs, key=lambda x: x[0])
	return min_cost[0] + this_value

result = cost((0, 0), ())-grid[0][0]
print(f'Risk of path: {result}')

# for y in range(10):
# 	for x in range(10):
# 		print(f'\033[1m{grid[x][y]}\033[0m' if (x, y) in path else grid[x][y], end=' ')
# 	print()
# print()