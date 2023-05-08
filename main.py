import json
import os 
from pathlib import Path







def processJson(jsonFolder):
    labellist = []
    for roots,dirs,files in os.walk(jsonFolder):
        for file in files:
            if file.endswith(".json"):
                jsonFile = json.load(open(os.path.join(roots,file)))
                for label in jsonFile["shapes"]:
                    labellist.append(label["label"])
    labellist = sorted(set(labellist))
    print(labellist)
def main(labelFolder): 
    processJson(labelFolder)

main("test")
