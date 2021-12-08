with open('data.txt') as data_file:
    lines = data_file.read().split('\n')

lines = [[y.split() for y in x.split('|')] for x in lines]

print(sum([len([num for num in line[1] if len(num) in [2, 3, 4, 7]]) for line in lines]))
