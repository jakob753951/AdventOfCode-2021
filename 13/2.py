with open('data.txt') as data_file:
	dots, folds = data_file.read().split('\n\n')
	dots = [[int(coord) for coord in dot.split(',')] for dot in dots.split('\n')]

	folds = [[0 if fold.split('=')[0][-1] == 'x' else 1, int(fold.split('=')[1])] for fold in folds.split('\n')]

def fold(axis, coord):
	for dot in dots:
		if dot[axis] > coord:
			dot[axis] = coord-(dot[axis]-coord)

for f in folds:
	fold(f[0], f[1])

for y in range(6):
	for x in range(39):
		print('█' if [x, y] in dots else '░', end='')
	print()