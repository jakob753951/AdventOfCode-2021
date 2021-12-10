with open('data.txt') as data_file:
    lines = data_file.read().split('\n')

def calc_line(line):
    stack = []
    value_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    opposites = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
            continue

        if opposites[char] == stack[-1]:
            stack.pop()
            continue

        return value_dict[char]

    return 0


result = sum([calc_line(line) for line in lines])
    
print(result)