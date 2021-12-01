with open('1-1/data.txt') as data_file:
	points = [int(p) for p in data_file.read().split('\n')]

points_sums = [p+points[i+1]+points[i+2] for i, p in enumerate(points) if i < len(points)-2]

pairs = list(zip(points_sums, points_sums[1:] + points_sums[:1]))[:-1]

ascending = sum(pair[0] < pair[1] for pair in pairs)

print(ascending)