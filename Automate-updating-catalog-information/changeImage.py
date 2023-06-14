#!/usr/bin/env python3
from PIL import Image
import os

img_src = "/home/{}/supplier-data/images".format(os.environ.get('USER'))

for file in os.listdir(img_src):
    try:
        img = Image.open(img_src + "/" + file).convert("RGB") #print(img)
        new_img = img.resize((600,400))
        new_img.save(img_src + "/" + file.replace("tiff","jpeg"))
    except:
        print("Skipping: " + file)
