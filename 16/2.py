from functools import reduce, partial

with open('data.txt') as data_file:
	bits = ''.join([bin(int(char, 16))[2:].zfill(4) for char in data_file.read()])

offset = 0

def parse_literal():
	global offset
	packet_bits = bits[offset:]
	end = False
	i = 0

	result = ""

	while not end:
		group = packet_bits[i*5:i*5+5]
		if group[0] == '0':
			end = True
		result += group[1:]
		i += 1
	offset += i*5
	return int(result, 2)

def parse_operator(type: int):
	global offset
	packet_bits = bits[offset:]
	length_type = int(packet_bits[0], 2)
	numbers = []
	if length_type == 1:
		number_of_sub_packets = int(packet_bits[1:12], 2)
		offset += 12
		for _ in range(number_of_sub_packets):
			numbers.append(parse_packet())
	else:
		bits_in_packets = int(packet_bits[1:16], 2)
		offset += 16
		starting_offset = offset
		while offset - starting_offset < bits_in_packets:
			numbers.append(parse_packet())
		
	operations = {
		0: sum,
		1: partial(reduce, lambda x, y: x*y),
		2: min,
		3: max,
		5: lambda nums: int(nums[0] > nums[1]),
		6: lambda nums: int(nums[0] < nums[1]),
		7: lambda nums: int(nums[0] == nums[1])
	}

	func = operations[type]
	result = func(numbers)
	return result


def parse_packet():
	global offset
	packet_bits = bits[offset:]

	version = int(packet_bits[:3], 2)
	type = int(packet_bits[3:6], 2)

	offset += 6

	if type == 4:
		result = parse_literal()
	else:
		result = parse_operator(type)
	return result


final_value = parse_packet()
print(final_value)