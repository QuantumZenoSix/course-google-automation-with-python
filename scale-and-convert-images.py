#!/usr/bin/env python3
import os
from PIL import Image

img_src = "/home/student-01-e20131f09923/supplier-data/images"

for file in os.listdir(img_src):
    try:
        img = Image.open("./images/" + file).convert("RGB") #print(img)
        new_img = img.resize((600,1400))
        new_img.save(img_src + "/" + file + ".jpeg")
    except:
        print("Skipping: " + file)
