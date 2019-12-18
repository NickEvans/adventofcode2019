import sys
import math

def writeVisible(layers, i):
    for la in layers:
        pixel = la[i]
        if pixel == '2':
            continue
        else:
            return pixel


file = open(sys.argv[1])
img = file.read()

#Image is 25 pixels wide and 6 pixels tall
imgX = 25
imgY = 6

#Number of digits that compose a layer
layerSize = imgX * imgY

#Split input by layers
layerList = [img[i:i + layerSize] for i in range(0, len(img), layerSize)]

#Determine visible pixels
decodedImg = []

for i in range(layerSize):
        decodedImg.append(writeVisible(layerList, i))

decodedImgRows = [decodedImg[i:i + imgX] for i in range(0, len(decodedImg), imgX)]

for row in decodedImgRows:
    print("".join(row).replace('0',' ').replace('1','O'))