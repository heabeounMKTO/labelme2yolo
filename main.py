import json
import os
from pathlib import Path
from fileutils import fileUtils as fu
from labelme2yolo import Labelme2Yolo as L2Y



    

def main():
    processFolder = "test"
    move = fu(processFolder, "export")

    move.createExportFolder()
    move.createLabelListFromFolder()
    
    label_list = move.loadLabelList()
    for file in os.listdir(processFolder):
        if file.endswith(".json"):
            loadjson = json.load(open(os.path.join(processFolder, file)))
            convert = L2Y(loadjson, label_list, processFolder)
            convert.convert2YOLO()
    move.moveAnnotationsToFolder()


main()
