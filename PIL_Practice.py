#!/usr/bin/env python3

#importing PIL for image manipulation, os for traversing directory
from PIL import Image
import PIL
import os

src = "/home/images"
dest = "/opt/icons/"
size = 128,128
#function takes path to an image as input. Flips, Resizes and Saves it in
#the /opt/icons/ folder in jpeg format. Has no return
def FlReSa(imf):
  with Image.open(os.path.join(src,imf)) as im:
    im = im.rotate(90)               #rotating 90 degres clockwise
    im.thumbnail(size)            #resizing to 128 by 128 pixels
    ims = im.convert('YCbCr')
    ims.save(os.path.join(dest,imf),"JPEG")

#loop through every image in /images folder and pass them to FlReSa function
for img in os.listdir(src):
  if not img.startswith('.'):
    FlReSa(img)