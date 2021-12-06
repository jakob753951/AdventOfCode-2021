with open('data.txt') as data_file:
	state = [int(x) for x in data_file.read().split(',')]
counts = [state.count(i) for i in range(9)]

for i in range(256):
	counts = [counts[(i + 1) % len(counts)] for i in range(len(counts))]
	counts[6] += counts[8]

print(sum(counts))