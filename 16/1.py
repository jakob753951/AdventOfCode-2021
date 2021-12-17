with open('data.txt') as data_file:
	bits = ''.join([bin(int(char, 16))[2:].zfill(4) for char in data_file.read()])

version_sum = 0

def parse_literal(offset: int):
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
	end_offset = offset + (i*5)
	return end_offset

def parse_operator(offset: int):
	packet_bits = bits[offset:]
	length_type = int(packet_bits[0], 2)
	if length_type == 1:
		number_of_sub_packets = int(packet_bits[1:12], 2)
		next_offset = offset + 12
		while number_of_sub_packets > 0:
			next_offset = parse_packet(next_offset)
			number_of_sub_packets -= 1
		return next_offset
	else:
		bits_in_packets = int(packet_bits[1:16], 2)
		next_offset = offset + 16
		while next_offset - (offset + 16) < bits_in_packets:
			next_offset = parse_packet(next_offset)
		return next_offset


def parse_packet(offset: int):
	global version_sum
	packet_bits = bits[offset:]

	version = int(packet_bits[:3], 2)
	version_sum += version
	type = int(packet_bits[3:6], 2)

	if type == 4:
		next_offset = parse_literal(offset+6)
	else:
		next_offset = parse_operator(offset+6)
	
	return next_offset


final_offset = parse_packet(0)
print(version_sum)