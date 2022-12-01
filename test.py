from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import imutils
from imutils import contours
from cv2 import imwrite

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = cv.imread('images/challenge2.jpg',0)
