with open('data.txt') as data_file:
	crabs = [int(p) for p in data_file.read().split(',')]

costs = [sum(abs(i-crab) for crab in crabs) for i in range(min(crabs), max(crabs)+1)]

print(min(costs))