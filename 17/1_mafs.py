with open('data.txt') as data_file:
	y0 = int(data_file.read().split('y=')[1].split('..')[0])
print(int(((abs(y0)-1)**2+(abs(y0)-1))/2))