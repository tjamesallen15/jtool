import cv2
import pytesseract
from pytesseract import image_to_string

import cv2
import glob
import numpy as np
import ntpath
import pytesseract
from PIL import Image
import cv2
import numpy as np
import pytesseract
import os, re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



# sImagesPath = 'captcha/captcha3.jpg'
# mylist = []

# def replace_chars(text):
#     list_of_numbers = re.findall(r'\d+', text)
#     result_number = ''.join(list_of_numbers)
#     return result_number

# for root, dirs, file_names in os.walk(sImagesPath):
#     for file_name in file_names:
#         img = cv2.imread(sImagesPath + file_name)
#         gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         thr = cv2.adaptiveThreshold(gry, 181, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 10)
#         txt = pytesseract.image_to_string(thr, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
#         mylist.append(replace_chars(txt))
#         print(replace_chars(txt))

# with open('Output.txt', 'w') as f:
#     for i in mylist:
#         s = ''.join(map(str, i))
#         f.write(s + '\n')



# img = cv2.imread("captcha/captcha3.jpg")
# gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# (h, w) = gry.shape[:2]
# gry = cv2.resize(gry, (w*2, h*2))
# cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
# thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# txt = image_to_string(thr)
# print(txt)



# IMAGES = ['img/captcha.png', 'img/captcha2.png', 'img/captcha3.png']
# symbols = glob.glob('lib/*.png')


# def guess_captcha(image):
#     image = Image.open(image)
#     pixels = image.load()
#     size = image.size

#     # Cleanup background noises from captcha
#     for x in range(size[0]):
#         for y in range(size[1]):
#             if pixels[x, y][0] < 120:
#                 pixels[x, y] = (0, 0, 0)
#             else:
#                 pixels[x, y] = (255, 255, 255)

#     # Search symbols in captcha
#     image = numpy.array(image)
#     result = []
#     for symbol in symbols:
#         img_symbol = cv2.imread(symbol)
#         match = cv2.matchTemplate(img_symbol, image, cv2.TM_CCOEFF_NORMED)
#         if len(match):
#             _, quality, _, location = cv2.minMaxLoc(match)
#             if quality > 0.8:
#                 result.append({'x': location[0], 'symbol': ntpath.basename(symbol).replace('.png', '')})
#     result = sorted(result, key=lambda k: k['x'])
#     return ''.join([x['symbol'] for x in result])


# for img in IMAGES:
#     print('{} -> {}'.format(img, guess_captcha(img)))