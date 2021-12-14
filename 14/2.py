from typing import Counter
import functools

with open('data.txt') as data_file:
    data, rules = data_file.read().split('\n\n')
data = list(data)
rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules.split('\n')}


@functools.cache
def calc_counts(pair, step):
	if step == 0 or pair not in rules:
		return Counter(pair)

	counts = Counter() \
		+ calc_counts(pair[0]+rules[pair], step-1) \
		+ calc_counts(rules[pair]+pair[1], step-1)
	counts[rules[pair]] -= 1
	return counts

pairs = list(zip(data, data[1:]))

counts = Counter()
for pair in pairs:
	counts += calc_counts(''.join(pair), 40)
counts -= Counter(data[1:-1])

print(max(counts.values()) - min(counts.values()))


