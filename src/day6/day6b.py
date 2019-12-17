import sys

class Planet:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

def depthToNode(node, top):
    if node.parent is None:
        return 0
    if node.parent is top:
        return 0
    return 1 + depthToNode(node.parent, top)

def sumDepths(plst):
    total = 0
    for p in plst:
        total += depthToNode(plst[p], planetMap["COM"])
    return total

def findCommonParent():
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
            return elem #The first common planet provides a path
    
    print("Error: no path found")

#Open and parse file
file = open(sys.argv[1])
buffer = file.read()
orbitList = buffer.split('\n')
for i in range(len(orbitList)):
    orbitList[i] = orbitList[i].split(')')

planetMap = {} #Name hashes to planet object

#Read all planets
for planets in orbitList:
    for i in range(2):
        if planets[i] not in planetMap:
            planetMap[planets[i]] = Planet(planets[i])

#Connect all planets:
for p in orbitList:
    planetMap[p[0]].children.append(planetMap[p[1]])
    planetMap[p[1]].parent = planetMap[p[0]]

#The first common parent planet between you and santa provides a bridge with the shortest path (because each planet only orbits one other planet)
print(depthToNode(planetMap["YOU"], planetMap[findCommonParent()]) + depthToNode(planetMap["SAN"], planetMap[findCommonParent()]))