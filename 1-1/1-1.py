with open('1-1/data.txt') as data_file:
	points = [int(p) for p in data_file.read().split('\n')]

pairs = list(zip(points, points[1:] + points[:1]))[:-1]

ascending = sum(pair[0] < pair[1] for pair in pairs)

print(ascending)