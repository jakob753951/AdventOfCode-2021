counts = [0] * 12

with open('data.txt') as data_file:
	numbers = data_file.read().split('\n')

for number in numbers:
	for i, digit in enumerate(number):
		counts[i] += int(digit)

print(counts)

gamma_digits = [int(count>(len(numbers)/2)) for count in counts]
epsilon_digits = [int(not count>(len(numbers)/2)) for count in counts]

print(gamma_digits)
print(epsilon_digits)

gamma = int(''.join(str(digit) for digit in gamma_digits), 2)
epsilon = int(''.join(str(digit) for digit in epsilon_digits), 2)

print(gamma)
print(epsilon)

print(gamma * epsilon)