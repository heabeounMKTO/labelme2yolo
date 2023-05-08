import json
import os
from pathlib import Path
import math
import tqdm

testList = ["0.5", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Labelme2Yolo:
    def __init__(self, json, labellist):
        # self.jsonFilePath = Path(jsonFilePath)
        # self.jsonFile = json.load(open(self.jsonFilePath))
        self.jsonFile = json
        self.labellist = labellist

    def convert2YOLO(self):
        self.getLabelsFromJson()
        self.writeYOLOtoFile(self.yoloarr, self.filename)

    def getFilename(self):
        self.filename = os.path.splitext(self.jsonFile["imagePath"])[0] + ".txt"
        return self.filename
    
    def xyxy2xywh(self, xyxy):
        x1, y1 = xyxy[0]
        x2, y2 = xyxy[1]
        x_center = ((x1 + x2) / 2) / self.imageDimensions[0]
        y_center = ((y1 + y2) / 2) / self.imageDimensions[1]
        _w = (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) / self.imageDimensions[0]
        _h = (math.sqrt((x1 - x1) ** 2 + (y2 - y1) ** 2)) / self.imageDimensions[1]
        return x_center, y_center, _w, _h

    def getImageDimensions(self):
        imageWidth = self.jsonFile["imageWidth"]
        imageHeight = self.jsonFile["imageHeight"]
        self.imageDimensions = [imageWidth, imageHeight]
        return self.imageDimensions

    def getLabelsFromJson(self):
        self.yoloarr = []
        self.getImageDimensions()
        for labels in self.jsonFile["shapes"]:
            x1y1 = labels["points"][0]
            x2y2 = labels["points"][1]
            x, y, w, h = self.xyxy2xywh((x1y1, x2y2))
            labelclass = self.labellist.index(labels["label"])
            self.yoloarr.append([labelclass, x, y, w, h])
        return self.yoloarr

    def writeYOLOtoFile(self, yololabels, filename):
        print("Writing annoations to File...")
        with open(filename, "w") as f:
            for annotations in tqdm.tqdm(yololabels):
                f.write(str(annotations[0]))
                f.write(" ")
                f.write(str(annotations[1]))
                f.write(" ")
                f.write(str(annotations[2]))
                f.write(" ")
                f.write(str(annotations[3]))
                f.write(" ")
                f.write(str(annotations[4]))
                f.write("\n")


testjson = json.load(open("test2/lbm/dragon-1683001744714.json"))
test = Labelme2Yolo(testjson, testList)
test.getFilename()
