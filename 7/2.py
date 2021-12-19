with open('7/data.txt') as data_file:
	crabs = [int(p) for p in data_file.read().split(',')]


def f(x):
	return int((x**2+x)/2)

costs = [sum(f(abs(i-crab)) for crab in crabs) for i in range(min(crabs), max(crabs)+1)]

print(min(costs))