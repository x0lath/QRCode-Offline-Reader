#!/usr/bin/env python

import qrcode
import cv2
import sys

from PIL import Image

fname = sys.argv[1]

fpath = fname

im = cv2.imread(fpath)
detector = cv2.QRCodeDetector()
data = detector.detectAndDecode(im)
print(data[0])