nodes: dict[str, list[str]] = {}

with open('data.txt') as data_file:
	for line in data_file.read().split('\n'):
		parts = line.split('-')

		n1 = nodes.get(parts[0], [])
		n1.append(parts[1])
		nodes[parts[0]] = n1

		n2 = nodes.get(parts[1], [])
		n2.append(parts[0])
		nodes[parts[1]] = n2

paths: list[str] = []

def walk(node, path):
	if node == 'end':
		paths.append([*path, node])
		return
	for adjacent in nodes[node]:
		if adjacent in path and adjacent.islower():
			continue
		walk(adjacent, [*path, node])

walk('start', [])

print(len(paths))