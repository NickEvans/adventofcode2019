import sys

file = open(sys.argv[1])
buffer = file.read()
orbitList = buffer.split('\n')
for i in range(len(orbitList)):
    orbitList[i] = orbitList[i].split(')')

class Planet:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

def orbitDepth(node):
    if node.parent is None:
        return 0
    
    return 1 + orbitDepth(node.parent)

def totalOrbits(plst):
    total = 0
    for p in plst:
        total += orbitDepth(plst[p])
    return total

planetMap = {}

#Read all planets
for planets in orbitList:
    for i in range(2):
        if planets[i] not in planetMap:
            planetMap[planets[i]] = Planet(planets[i])

#Connect all planets:
for p in orbitList:
    planetMap[p[0]].children.append(planetMap[p[1]])
    planetMap[p[1]].parent = planetMap[p[0]]

print(totalOrbits(planetMap))