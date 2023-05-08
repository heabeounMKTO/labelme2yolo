import json
import os
from pathlib import Path
import tqdm
import shutil
import math


ext = [".jpeg", ".jpg", ".png"]


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
            os.makedirs(os.path.join("export/valid", labels))
        except FileExistsError:
            print("folder already exists!")

    def moveToFolder(self, jsonList, destinationFolder):
        def moveLabelandImage(annotation, foldername):
            orig_labels_path = os.path.join(self.processingFolder, annotation)
            matchedImage = str(findMatchingImage(annotation))
            orig_images_path = os.path.join(self.processingFolder, matchedImage)
            dest_labels_path = os.path.join(
                self.exportFolder, os.path.join(foldername, "labels")
            )
            
            dest_images_path = os.path.join(
                self.exportFolder, os.path.join(foldername, "images")
            )
            full_dest_label_path = os.path.join(dest_labels_path, annotation) 
            full_dest_image_path = os.path.join(dest_images_path, matchedImage)
            
            if os.path.exists(orig_images_path):
                shutil.move(orig_images_path, full_dest_image_path)
            else:
                pass 
            if os.path.exists(orig_labels_path):
                shutil.move(orig_labels_path, full_dest_label_path)
            else:
                pass
                

        def findMatchingImage(annotation):
            for file in self.allfiles:
                if file.endswith(tuple(ext)):
                    if os.path.splitext(file)[0] == os.path.splitext(annotation)[0]:
                        if file != None:
                            return file


        match destinationFolder:
            case "train":
                print("train set")
                for index in tqdm.tqdm(range(0, self.train_number - 1)):
                    moveLabelandImage(jsonList[index], "train")
            case "valid":
                print("valid set")
                for index in tqdm.tqdm(range(
                    (self.train_number), (self.train_number + self.val_number) - 1
                )):
                    moveLabelandImage(jsonList[index], "valid")
            case "test":
                print("test set")
                for index in tqdm.tqdm(range(
                    (self.train_number + self.val_number),
                    (self.train_number + self.val_number + self.test_number) - 1,
                )):
                    moveLabelandImage(jsonList[index], "test")

    def moveAnnotationsToFolder(self, train_split=75, val_split=15, test_split=10):
        jsonfiles = []
        self.allfiles = []
        for file in os.listdir(self.processingFolder):
            self.allfiles.append(file)
            if file.endswith(".txt"):
                jsonfiles.append(file)
        self.train_number = math.floor((len(jsonfiles)) * train_split / 100)
        self.val_number = math.floor((len(jsonfiles)) * val_split / 100)
        self.test_number = math.floor((len(jsonfiles)) * test_split / 100)

        self.moveToFolder(jsonfiles, "train")
        self.moveToFolder(jsonfiles, "valid")
        self.moveToFolder(jsonfiles, "test")
