with open('data.txt') as data_file:
	instructions = [p.split(' ') for p in data_file.read().split('\n')]

instructions = [(a, int(b)) for a, b in instructions]

instructions_map = {
	'down': lambda x: x,
	'up': lambda x: -x
}

aim = 0
depth = 0
h_pos = 0
for inst, x in instructions:
	if inst in instructions_map:
		aim += instructions_map[inst](x)
	else:
		h_pos += x
		depth += aim * x

print(f'{depth} * {h_pos} = {depth * h_pos}')
