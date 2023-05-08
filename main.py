import json
import os
from pathlib import Path
from fileutils import fileUtils as fu
from labelme2yolo import Labelme2Yolo as L2Y



testlabellist = ['0.5','1','2','3','4','5','6','7','8','9']

def main(labelFolder):
    
    processFolder = "test"
    
    move = fu(processFolder, "export")

    for file in os.listdir(processFolder):
        if file.endswith(".json"):
            loadjson = json.load(open(os.path.join(processFolder,file)))
            convert = L2Y(loadjson,testlabellist,processFolder)
            convert.convert2YOLO()

    move.moveAnnotationsToFolder()


main("test")
