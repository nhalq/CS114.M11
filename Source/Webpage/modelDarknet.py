from operator import mod
import os
import cv2
import numpy as np

from config import *
from modelYOLO import modelYOLO

FILENAME_CONFIG = os.path.join('model', 'yolov4.cfg')
FILENAME_WEIGHT = os.path.join('model', 'yolov4_last.weights')

class modelDarknet:
    def __init__(self):
        self.net = cv2.dnn.readNetFromDarknet(
            FILENAME_CONFIG, FILENAME_WEIGHT)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def predict(self, image):
        H, W = image.shape[:2]
        blob = cv2.dnn.blobFromImage(
            image, 1/255.0, (416, 416), swapRB=True, crop=False)

        self.net.setInput(blob)
        outputs = self.net.forward(self.ln)
        outputs = np.vstack(outputs)

        conf = CFG_THRESHOLD
        boxes = list()
        confidences = list()
        for output in outputs:
            scores = output[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > conf:
                x, y, w, h = output[:4] * np.array([W, H, W, H])
                p0 = int(x - w//2), int(y - h//2)
                p1 = int(x + w//2), int(y + h//2)
                boxes.append([*p0, *p1])
                confidences.append(float(confidence))

        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf, conf-0.1)
        boxes = np.array(boxes)[indices.flatten()]
        return boxes.tolist()

from apiProcess import *
if __name__ == '__main__':
    import cv2
    im = cv2.imread('IMG_0017_jpg.rf.087aca81dd5ffadd9b19734d8ff3e2a7.jpg')
    model = modelDarknet()
    lc = model.predict(im)
    _abc = convertImage(im, lc).averageBlur(10)
    cv2.imshow(_abc)
    cv2.waitKey()
