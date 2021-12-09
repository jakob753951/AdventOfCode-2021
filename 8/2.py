with open('data.txt') as data_file:
    lines = data_file.read().split('\n')

lines = [[y.split() for y in x.split('|')] for x in lines]

def get_translation_dict(samples):
	one = next(num for num in samples if len(num) == 2)
	four = next(num for num in samples if len(num) == 4)
	seven = next(num for num in samples if len(num) == 3)

	counts = [''.join(samples).count(char) for char in 'abcdefg']

	a = next(seg for seg in seven if seg not in one)
	b = 'abcdefg'[counts.index(6)]
	c = next('abcdefg'[i] for i, count in enumerate(counts) if count == 8 and 'abcdefg'[i] != a)
	d = next('abcdefg'[i] for i, count in enumerate(counts) if count == 7 and 'abcdefg'[i] in four)
	e = 'abcdefg'[counts.index(4)]
	f = 'abcdefg'[counts.index(9)]
	g = next('abcdefg'[i] for i, count in enumerate(counts) if count == 7 and 'abcdefg'[i] not in four)

	return {
		a: 'a',
		b: 'b',
		c: 'c',
		d: 'd',
		e: 'e',
		f: 'f',
		g: 'g'
	}

def translate(letters, translation_dict):
	return ''.join([translation_dict[letter] for letter in letters])

def calc_line(samples, numbers):
	translation_dict = get_translation_dict(samples)
	digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
	return sum((10**i * digits.index(''.join(sorted(translate(jumble, translation_dict))))) for i, jumble in enumerate(reversed(numbers)))

final = sum(calc_line(line[0], line[1]) for line in lines)

print(final)