import numpy as np
import math

#read in input
with open("inputs/day_15.txt") as reader:
	lines = reader.readlines()

information = []
sensor_x_mins = []
sensor_x_maxs = []
sensor_y_mins = []
sensor_y_maxs = []

#parse input
for line in lines:
	line = line.strip()
	line = line.split()
	sensor_x = int(line[2][2:len(line[2])-1])
	sensor_y = int(line[3][2:len(line[3])-1])
	beacon_x = int(line[8][2:len(line[8])-1])
	beacon_y = int(line[9][2:len(line[9])])
	dx = abs(sensor_x - beacon_x)
	dy = abs(sensor_y - beacon_y)
	d_total = dx + dy
	x_max = sensor_x + d_total
	x_min = sensor_x - d_total
	y_max = sensor_y + d_total
	y_min = sensor_y - d_total
	sensor_x_mins.append(x_min)
	sensor_x_maxs.append(x_max)
	sensor_y_mins.append(y_min)
	sensor_y_maxs.append(y_max)
	information.append([sensor_x,sensor_y,beacon_x,beacon_y,dx,dy])

x_min = min(sensor_x_mins)
x_max = max(sensor_x_maxs)
y_min = min(sensor_y_mins)
y_max = max(sensor_y_maxs)

print(x_max,x_min,y_max,y_min, flush = True)

total_columns = x_max-x_min + 1
total_rows = y_max - y_min + 1
x_offset = x_min
y_offset = y_min

print(total_columns,total_rows, flush = True)
def function(row_int):
	row_of_interest = row_int
	act_row = row_of_interest - y_offset 


	grid = []

	for y in range(1):
		row = []
		for x in range(total_columns):
			row.append('.')
		grid = row

	#print("grid done")
	np.savetxt("Output.txt",np.array(grid), fmt = '%s')

	for entry in information:
		#print(entry, flush = True)
		sensor_x = entry[0] - x_offset
		sensor_y = entry[1] - y_offset
		beacon_x = entry[2] - x_offset
		beacon_y = entry[3] - y_offset
		if sensor_y == act_row:
			grid[sensor_x] = "S"
		if beacon_y == act_row:
			grid[beacon_x] = "B"

	#print("here", flush = True)

	for entry in information:
		#print(entry, flush = True)
		sensor_x = entry[0] - x_offset
		sensor_y = entry[1] - y_offset
		beacon_x = entry[2] - x_offset
		beacon_y = entry[3] - y_offset
		dx = abs(sensor_x - beacon_x)
		dy = abs(sensor_y - beacon_y)
		d_total = dx + dy
		x_max = sensor_x + d_total
		x_min = sensor_x - d_total
		y_max = sensor_y + d_total
		y_min = sensor_y - d_total

		if (act_row >= y_min) and (act_row <= y_max):
			dist_to_row = abs(sensor_y - act_row)
			dist_x = d_total - dist_to_row
			for x in range(sensor_x - dist_x,sensor_x + dist_x + 1):
				if grid[x] == ".":
					grid[x] = "#"

	count = 0
	for x in range(len(grid)):
		if grid[x] == '#' or grid[x] == "S":
			count += 1

	#print(row)
	print(count)

	np.savetxt("Output.txt",np.array(grid),fmt = "%s")

function(2000000)
