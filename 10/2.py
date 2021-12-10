with open('data.txt') as data_file:
    lines = data_file.read().split('\n')

def calc_line(line):
    stack = []
    value_dict = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    opposites = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
            continue

        if char == opposites[stack[-1]]:
            stack.pop()
            continue

        return 0

    score = 0
    for char in reversed(stack):
        score = score * 5 + value_dict[char]
    return score

scores = [calc_line(line) for line in lines]

scores = [x for x in scores if x != 0]

result = sorted(scores)[len(scores)//2]
    
print(result)