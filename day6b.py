import sys

file = open(sys.argv[1])
buffer = file.read()
orbitList = buffer.split('\n')
for i in range(len(orbitList)):
    orbitList[i] = orbitList[i].split(')')

planetMap = {}

class Planet:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

def orbitDepth(node, top):
    if node.parent is None:
        return 0
    if node.parent is top:
        return 0
    return 1 + orbitDepth(node.parent, top)

def totalOrbits(plst):
    total = 0
    for p in plst:
        total += orbitDepth(plst[p], planetMap["COM"])
    return total

#Read all planets
for planets in orbitList:
    for i in range(2):
        if planets[i] not in planetMap:
            planetMap[planets[i]] = Planet(planets[i])

#Connect all planets:
for p in orbitList:
    planetMap[p[0]].children.append(planetMap[p[1]])
    planetMap[p[1]].parent = planetMap[p[0]]

def commonPath():
    plst1 = []
    plst2 = []

    curP = planetMap["YOU"].parent.name
    while(curP != "COM"):
        curP = planetMap[curP].parent.name
        plst1.append(curP)
    
    curP = planetMap["SAN"].parent.name
    while(curP != "COM"):
        curP = planetMap[curP].parent.name
        plst2.append(curP)

    for elem in plst1:
        if elem in plst2:
            return elem

print(orbitDepth(planetMap["YOU"], planetMap[commonPath()]) + orbitDepth(planetMap["SAN"], planetMap[commonPath()]))