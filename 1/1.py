with open('data.txt') as data_file:
	points = [int(p) for p in data_file.read().split('\n')]

pairs = list(zip(points, points[1:]))

ascending = [pair[0] < pair[1] for pair in pairs].count(True)

print(ascending)