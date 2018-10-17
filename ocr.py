#Install Tessaract - https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
import argparse
import cv2
import os
import pytesseract

try:import Image
except ImportError:from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
print(pytesseract.image_to_string(Image.open('\Desktop\\img.jpg'), lang='eng'))
