import json
import os
from pathlib import Path
from fileutils import fileUtils as fu


def main(labelFolder):
    labeljsons = fu("test") 
    labeljsons = labeljsons.createLabelListFromFolder()
    print(labeljsons) 
main("test")
