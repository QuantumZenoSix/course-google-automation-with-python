#!/usr/bin/env python3
from PIL import Image
import os

student_id = "student-01-439710e8fd7b"
img_src = "/home/{}/supplier-data/images".format(student_id)

for file in os.listdir(img_src):
    try:
        img = Image.open(img_src + "/" + file).convert("RGB") #print(img)
        new_img = img.resize((600,400))
        new_img.save(img_src + "/" + file.replace("tiff","jpeg"))
    except:
        print("Skipping: " + file)
