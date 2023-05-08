import json
import os 
from pathlib import Path

class Labelme2Yolo:
    def __init__(self, jsonFilePath):
        self.jsonFilePath = Path(jsonFilePath)
        self.jsonFile = json.load(open(self.jsonFilePath))
    
    def getImageDimensions(self):
        imageWidth = self.jsonFile["imageWidth"]
        imageHeight = self.jsonFile["imageHeight"]
        self.imageDimensions = [imageWidth,imageHeight]
        return self.imageDimensions

    def getLabelsFromJson(self):
        labelsarr = [] 
        for labels in self.jsonFile["shapes"]: 
            labelsarr.append(labels["points"])
        print(labelsarr)
        return labelsarr

test = Labelme2Yolo("test/dragon-1683001744714.json")
test.getLabelsFromJson()
