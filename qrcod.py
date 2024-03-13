#!/usr/bin/env python

import qrcode
import cv2
import sys

from PIL import Image

fpath = sys.argv[1]

im = cv2.imread(fpath)
detector = cv2.QRCodeDetector()
data = detector.detectAndDecode(im)
print(data[0])
