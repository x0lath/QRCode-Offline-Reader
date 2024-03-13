#!/usr/bin/env python

import cv2
import sys

from PIL import Image

fpath = sys.argv[1]

qr = cv2.imread(fpath)
detector = cv2.QRCodeDetector()
data = detector.detectAndDecode(qr)
print(data[0])
