from typing import Counter


with open('data.txt') as data_file:
    data, rules = data_file.read().split('\n\n')
data = list(data)
rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules.split('\n')}


def step():
	global data
	pairs = list(zip(data, data[1:]))
	data = [data[0]]
	for pair in pairs:
		if ''.join(pair) in rules:
			data.append(rules[''.join(pair)])
			data.append(pair[1])

for i in range(10):
	step()

counts = Counter(data)

print(max(counts.values()) - min(counts.values()))


