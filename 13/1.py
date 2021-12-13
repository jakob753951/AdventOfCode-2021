with open('data.txt') as data_file:
	dots, folds = data_file.read().split('\n\n')
	dots = [[int(coord) for coord in dot.split(',')] for dot in dots.split('\n')]

	folds = [[0 if fold.split('=')[0][-1] == 'x' else 1, int(fold.split('=')[1])] for fold in folds.split('\n')]

def fold(axis, coord):
	for dot in dots:
		if dot[axis] > coord:
			dot[axis] = coord-(dot[axis]-coord)

fold(folds[0][0], folds[0][1])

# for f in folds:
# 	fold(f[0], f[1])

dots = set(tuple(x) for x in dots)

print(len(dots))