import sys

file = open(sys.argv[1])
buffer = file.read()
buffer = buffer.split('\n')

wire1 = buffer[0].split(',')
wire2 = buffer[1].split(',')

intersections = {} #List of intersections
wirepoints = {} #Every point on the grid the first wire covers
wirelength = 0 #Current no. of steps
coord = (0, 0) #Current X and Y coordinate

for lines in wire1:
    if lines[0] == 'U':
        for _ in range(int(lines[1:])):
            coord = (coord[0], coord[1] + 1)
            wirelength += 1
            if coord not in wirepoints:
                wirepoints[coord] = wirelength
    elif lines[0] == 'D':
        for _ in range(int(lines[1:])):
            coord = (coord[0], coord[1] - 1)
            wirelength += 1
            if coord not in wirepoints:
                wirepoints[coord] = wirelength
    elif lines[0] == 'L':
        for _ in range(int(lines[1:])):
            coord = (coord[0] - 1, coord[1])
            wirelength += 1
            if coord not in wirepoints:
                wirepoints[coord] = wirelength
    elif lines[0] == 'R':
        for _ in range(int(lines[1:])):
            coord = (coord[0] + 1, coord[1])
            wirelength += 1
            if coord not in wirepoints:
                wirepoints[coord] = wirelength

coord = [0, 0] #Reset at central port
wirelength = 0
for lines in wire2:
    if lines[0] == 'U':
        for _ in range(int(lines[1:])):
            coord = (coord[0], coord[1] + 1)
            wirelength += 1
            if coord in wirepoints:
                if coord not in intersections:
                    intersections[coord] = (wirepoints[coord] + wirelength)
    elif lines[0] == 'D':
        for _ in range(int(lines[1:])):
            coord = (coord[0], coord[1] - 1)
            wirelength += 1
            if coord in wirepoints:
                if coord not in intersections:
                    intersections[coord] = (wirepoints[coord] + wirelength)
    elif lines[0] == 'L':
        for _ in range(int(lines[1:])):
            coord = (coord[0] - 1, coord[1])
            wirelength += 1
            if coord in wirepoints:
                if coord not in intersections:
                    intersections[coord] = (wirepoints[coord] + wirelength)
    elif lines[0] == 'R':
        for _ in range(int(lines[1:])):
            coord = (coord[0] + 1, coord[1])
            wirelength += 1
            if coord in wirepoints:
                if coord not in intersections:
                    intersections[coord] = (wirepoints[coord] + wirelength)

shortest = float("inf")
for p in intersections:
    if(intersections[p]) < shortest:
        shortest = intersections[p]

print(shortest)
