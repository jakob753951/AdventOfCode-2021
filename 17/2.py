import re
from math import ceil, sqrt

pattern = re.compile(r'target area: x=(?P<x0>-?[0-9]+)\.\.(?P<x1>-?[0-9]+), y=(?P<y0>-?[0-9]+)\.\.(?P<y1>-?[0-9]+)')

with open('data.txt') as data_file:
	matches = pattern.match(data_file.read())
	x0 = int(matches.group('x0'))
	x1 = int(matches.group('x1'))
	y0 = int(matches.group('y0'))
	y1 = int(matches.group('y1'))

def check_velocity(x, y):
	vel_x, vel_y = max(0, x-1), y-1
	pos_x, pos_y = x, y
	while pos_x <= x1 and pos_y >= y0:
		if x0 <= pos_x <= x1 and y0 <= pos_y <= y1:
			return True
		pos_x, pos_y, vel_x, vel_y = pos_x + vel_x, pos_y + vel_y, max(0, vel_x-1), vel_y-1
	return False


def g(x):
	return -1+sqrt(1+8*x)/2

min_x = ceil(g(x0))
max_x = x1
min_y = y0
max_y = abs(y0)-1

sum = 0
for y in range(min_y, max_y+1):
	for x in range(min_x, max_x+1):
		if check_velocity(x, y):
			sum += 1

print(sum)