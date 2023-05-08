import json
import os
from pathlib import Path
from fileutils import fileUtils as fu
from labelme2yolo import Labelme2Yolo as L2Y
import typer


def initConversion(processFolder, exportFolder):
    file_utils = fu(processFolder,exportFolder)
    file_utils.createExportFolder()
    file_utils.createLabelListFromFolder()
    return file_utils

def main(input: str, output: str):
    initconv = initConversion(input, output)
    label_list = initconv.loadLabelList()
    for file in os.listdir(input):
        if file.endswith(".json"):
            loadjson = json.load(open(os.path.join(input, file)))
            convert = L2Y(loadjson, label_list, input)
            convert.convert2YOLO()
    initconv.moveAnnotationsToFolder()

if __name__ == "__main__":
    typer.run(main)
