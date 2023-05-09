import albumentations as A
import cv2


class augmentImage:
    def __init__(self, imagePath):
        self.image = cv2.imread(imagePath)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) 
    def numpyArr(self):
        transform = A.Compose([
            A.ChannelDropoff()
            ], bbox_param=A.BboxParams(format='yolo'))
        bboxes = 

test = augmentImage("test/dragon-1683001744714.jpeg")

