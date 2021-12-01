with open('1-1/data.txt') as data_file:
	points = [int(p) for p in data_file.read().split('\n')]

points_sums = [sum(points[i:i+3]) for i in range(len(points)-2)]

pairs = list(zip(points_sums, points_sums[1:] + points_sums[:1]))[:-1]

ascending = sum(pair[0] < pair[1] for pair in pairs)

print(ascending)