import sys
import math

file = open(sys.argv[1])
img = file.read()

#Image is 25 pixels wide and 6 pixels tall
imgX = 25
imgY = 6

#Number of digits that compose a layer
layerSize = imgX * imgY

#Split input by layers
layerList = [img[i:i + layerSize] for i in range(0, len(img), layerSize)]

fewestZeroes = math.inf
chosenLayer = 0
i = 0
for layer in layerList:
    numZeroes = layer.count('0')
    if numZeroes < fewestZeroes:
        fewestZeroes = numZeroes
        chosenLayer = layerList[i]
    i = i + 1

solution = chosenLayer.count('1') * chosenLayer.count('2')
print(solution)