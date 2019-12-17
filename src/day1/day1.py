import sys

filepath = sys.argv[1]
file = open(filepath)

fuel = 0

for line in file:
    fuel += (int(line) / 3) - 2

print(fuel)

file.close()