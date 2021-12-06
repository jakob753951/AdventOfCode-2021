with open('data.txt') as data_file:
	state = [int(x) for x in data_file.read().split(',')]

for i in range(80):
	to_append = state.count(0)
	state = [cell-1 if cell-1 >= 0 else 6 for cell in state]
	state.extend([8]*to_append)
	print(i)

print(len(state))