import json
import os 
from pathlib import Path
import tqdm

class fileUtils():
    def __init__(self, processingFolder):
        self.processingFolder = processingFolder

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

        
