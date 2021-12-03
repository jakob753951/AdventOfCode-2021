with open('3/data.txt') as data_file:
	oxygen = co2 = data_file.read().split('\n')

def get_counts(arr):
	counts = [0] * 12
	for number in arr:
		for i, digit in enumerate(number):
			counts[i] += int(digit)
	return counts

for i in range(12):
	if len(oxygen) != 1:
		oxy_count = get_counts(oxygen)
		oxygen = [num for num in oxygen if int(num[i]) == int(oxy_count[i]>=(len(oxygen)/2))]
	if len(co2) != 1:
		co2_count = get_counts(co2)
		co2 = [num for num in co2 if int(num[i]) == int(co2_count[i]<(len(co2)/2))]

oxygen_generator_rating = int(oxygen[0], 2)
CO2_scrubber_rating = int(co2[0], 2)

print(f'{oxygen_generator_rating} * {CO2_scrubber_rating} = {oxygen_generator_rating * CO2_scrubber_rating}')
