import sys

filepath = sys.argv[1]
file = open(filepath)

fuel = 0

def addFuel(mass):
    f = (mass / 3) - 2
    if f <= 0:
        return 0
    return f + addFuel(f)

for line in file:
    fuel += addFuel(int(line))

print(fuel)

file.close()