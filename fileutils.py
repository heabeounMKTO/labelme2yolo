import json
import os
from pathlib import Path
import tqdm
import shutil
import math

class fileUtils:
    def __init__(self, processingFolder, exportFolder):
        self.processingFolder = processingFolder
        self.exportFolder = exportFolder

    def createLabelListFromFolder(self):
        jsonlist = []
        for roots, dirs, files in os.walk(self.processingFolder):
            for file in files:
                if file.endswith(".json"):
                    jsonFile = json.load(open(os.path.join(roots, file)))
                    for label in jsonFile["shapes"]:
                        jsonlist.append(label["label"])
        jsonlist = sorted(set(jsonlist))
        return jsonlist

    def createExportFolder(self):
        images = "images"
        labels = "labels"
        try:
            os.makedirs(os.path.join("export/test", images))
            os.makedirs(os.path.join("export/test", labels))
        except FileExistsError:
            print("folder already exists!")
        try:
            os.makedirs(os.path.join("export/train", images))
            os.makedirs(os.path.join("export/train", labels))
        except FileExistsError:
            print("folder already exists!")
        try:
            os.makedirs(os.path.join("export/valid", images))
            os.makedirs(os.path.join("expost/valid", labels))
        except FileExistsError:
            print("folder already exists!")

    def moveAnnotationsToFolder(self, train_split=75, val_split=15, test_split=10):
        jsonfiles = []
        for file in os.listdir(self.processingFolder):
            if file.endswith(".json"):
                jsonfiles.append(file)
        train_number = math.floor((len(jsonfiles)) * train_split/100)
        val_number = math.floor((len(jsonfiles)) * val_split/100)
        test_number = math.floor((len(jsonfiles)) * test_split/100)
        print(train_number + val_number + test_number)
