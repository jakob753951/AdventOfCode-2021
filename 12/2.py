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

paths: set[str] = set()

def walk(node, path, small_cave, visited):
	if node == 'end':
		paths.add((*path, node))
		return
	for adjacent in nodes[node]:
		if small_cave == adjacent and not visited:
			walk(adjacent, [*path, node], small_cave, True)

		if adjacent in path and adjacent.islower():
			continue
		if adjacent.islower() and small_cave is None:
			walk(adjacent, [*path, node], adjacent, visited)
		walk(adjacent, [*path, node], small_cave, visited)

walk('start', [], None, False)

print(len(paths))