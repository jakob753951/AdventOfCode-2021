import re

pattern = re.compile(r'target area: x=(?P<x0>-?[0-9]+)\.\.(?P<x1>-?[0-9]+), y=(?P<y0>-?[0-9]+)\.\.(?P<y1>-?[0-9]+)')

with open('data.txt') as data_file:
	matches = pattern.match(data_file.read())
	x0 = int(matches.group('x0'))
	x1 = int(matches.group('x1'))
	y0 = int(matches.group('y0'))
	y1 = int(matches.group('y1'))

def f(x):
	return int((x**2+x)/2)

vel_y = abs(y0)-1

max_y_from_vel = f(vel_y)
print(max_y_from_vel)




